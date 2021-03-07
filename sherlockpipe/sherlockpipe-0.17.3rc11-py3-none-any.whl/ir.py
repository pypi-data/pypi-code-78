import multiprocessing
import traceback
from argparse import ArgumentParser

import numpy as np
import os, sys
import ellc
from sherlockpipe.objectinfo.MissionInputObjectInfo import MissionInputObjectInfo
from sherlockpipe import sherlock
from sherlockpipe.scoring.QuorumSnrBorderCorrectedSignalSelector import QuorumSnrBorderCorrectedSignalSelector
from sherlockpipe.objectinfo.preparer.MissionLightcurveBuilder import MissionLightcurveBuilder
from sherlockpipe.objectinfo.MissionObjectInfo import MissionObjectInfo
import wotan
from transitleastsquares import transitleastsquares
from transitleastsquares import transit_mask, cleaned_array
from transitleastsquares import catalog_info
import astropy.constants as ac
import astropy.units as u
import lightkurve as lk
import os
import re
import pandas as pd
import shutil


class TIRMA:
    """
    TIRMA: Transit Inject and Recovery with Multi-phase Analysis
    """
    object_info = None

    def __init__(self, target, sectors, dir):
        self.id = target
        self.dir = dir
        self.sectors = sectors

    def __retrieve_object_data(self):
        self.object_info = MissionObjectInfo(self.id, self.sectors)
        lightcurve_builder = MissionLightcurveBuilder()
        self.lc, self.lc_data, self.star_info, self.transits_min_count, self.sectors, self.quarters = \
            lightcurve_builder.build(self.object_info, None)
        self.ab = self.star_info.ld_coefficients
        self.mass = self.star_info.mass
        self.massmin = self.star_info.mass_min
        self.massmax = self.star_info.mass_max
        self.radius = self.star_info.mass
        self.radiusmin = self.star_info.mass_min
        self.radiusmax = self.star_info.mass_max
        # units for ellc
        self.rstar = self.star_info.radius * u.R_sun
        self.mstar = self.star_info.mass * u.M_sun
        self.mstar_min = self.star_info.mass_min * u.M_sun
        self.mstar_max = self.star_info.mass_max * u.M_sun
        self.rstar_min = self.star_info.radius_min * u.R_sun
        self.rstar_max = self.star_info.radius_max * u.R_sun

    def __build_inject_dir(self):
        return self.dir + "/" + self.object_info.mission_id().replace(" ", "") + "_ir/"

    def inject(self, phases, min_period, max_period, step_period, min_radius, max_radius, step_radius):
        self.__retrieve_object_data()
        print('\n STELLAR PROPERTIES FOR THE SIGNAL SEARCH')
        print('================================================\n')
        print('limb-darkening estimates using quadratic LD (a,b)=', self.ab)
        print('mass =', format(self.mstar,'0.5f'))
        print('mass_min =', format(self.mstar_min,'0.5f'))
        print('mass_max =', format(self.mstar_max,'0.5f'))
        print('radius =', format(self.rstar,'0.5f'))
        print('radius_min =', format(self.rstar_min,'0.5f'))
        print('radius_max =', format(self.rstar_max,'0.5f'))
        lc_new = lk.LightCurve(time=self.lc.time, flux=self.lc.flux, flux_err=self.lc.flux_err)
        clean = lc_new.remove_outliers(sigma_lower=float('inf'), sigma_upper=3)
        flux0 = clean.flux.value
        time = clean.time.value
        flux_err = clean.flux_err.value
        inject_dir = self.__build_inject_dir()
        if os.path.isdir(inject_dir):
            shutil.rmtree(inject_dir)
        os.mkdir(inject_dir)
        for period in np.arange(min_period, max_period, step_period):
            for t0 in np.arange(time[60], time[60] + period - 0.1, period / phases):
                for rplanet in np.arange(min_radius, max_radius, step_radius):
                    rplanet = np.around(rplanet, decimals=2) * u.R_earth
                    print('\n')
                    print('P = ' + str(period) + ' days, Rp = ' + str(rplanet) + ", T0 = " + str(t0))
                    time_model, flux_model, flux_err_model = self.__make_model(time, flux0, flux_err, self.rstar,
                                                                               self.mstar, t0, period, rplanet)
                    file_name = os.path.join(inject_dir + '/P' + str(period) + '_R' + str(rplanet.value) + '_' + str(t0) +
                                             '.csv')
                    lc_df = pd.DataFrame(columns=['#time', 'flux', 'flux_err'])
                    lc_df['#time'] = time_model
                    lc_df['flux'] = flux_model
                    lc_df['flux_err'] = flux_err_model
                    lc_df.to_csv(file_name, index=False)
        return self

    def recovery(self, cores, sherlock_samples=3):
        if self.object_info is None:
            self.__retrieve_object_data()
        print('\n STELLAR PROPERTIES FOR THE SIGNAL SEARCH')
        print('================================================\n')
        print('limb-darkening estimates using quadratic LD (a,b)=', self.ab)
        print('mass =', format(self.mstar, '0.5f'))
        print('mass_min =', format(self.mstar_min, '0.5f'))
        print('mass_max =', format(self.mstar_max, '0.5f'))
        print('radius =', format(self.rstar, '0.5f'))
        print('radius_min =', format(self.rstar_min, '0.5f'))
        print('radius_max =', format(self.rstar_max, '0.5f'))
        reports_df = pd.DataFrame(columns=['period', 'radius', 'epoch', 'found', 'snr', 'sde', 'run'])
        #TODO allow addition of known_transits
        known_transits = []
        # known_transits = [{"T0": 2458684.832891 - 2450000, "P": 3.119035, "D": 1.271571 / 24},
        #                   {"T0": 2458687.539955 - 2450000, "P": 6.387611, "D": 1.246105 / 24}]
        inject_dir = self.__build_inject_dir()
        for file in os.listdir(inject_dir):
            if file.endswith(".csv"):
                try:
                    period = float(re.search("P([0-9]+\\.[0-9]+)", file)[1])
                    r_planet = float(re.search("R([0-9]+\\.[0-9]+)", file)[1])
                    epoch = float(re.search("_([0-9]+\\.[0-9]+)\\.csv", file)[1])
                    df = pd.read_csv(inject_dir + file, float_precision='round_trip', sep=',',
                                     usecols=['#time', 'flux', 'flux_err'])
                    if len(df) == 0:
                        found = True
                        snr = 20
                        sde = 20
                        run = 1
                    else:
                        lc = lk.LightCurve(time=df['#time'], flux=df['flux'], flux_err=df['flux_err'])
                        clean = lc.remove_nans().remove_outliers(sigma_lower=float('inf'),
                                                                 sigma_upper=3)  # remove outliers over 3sigma
                        flux = clean.flux.value
                        time = clean.time.value
                        intransit = self.__transit_masks(known_transits, time)
                        found, snr, sde, run = self.__tls_search(time, flux, self.radius, self.radiusmin,
                                                                 self.radiusmax, self.mass, self.massmin,
                                                                 self.massmax, self.ab, intransit, epoch, period, 0.5,
                                                                 45, 5, cores, "default")
                    new_report = {"period": period, "radius": r_planet, "epoch": epoch, "found": found, "snr": snr,
                                  "sde": sde, "run": run}
                    reports_df = reports_df.append(new_report, ignore_index=True)
                    print("P=" + str(period) + ", R=" + str(r_planet) + ", T0=" + str(epoch) + ", FOUND WAS " + str(
                        found) +
                          " WITH SNR " + str(snr) + " AND SDE " + str(sde))
                    reports_df.to_csv(inject_dir + "a_tls_report.csv", index=False)
                except Exception as e:
                    traceback.print_exc()
                    print("File not valid: " + file)
        if sherlock_samples > 0:
            report = {}
            reports_df = pd.DataFrame(columns=['period', 'radius', 'epoch', 'found', 'snr', 'sde', 'run'])
            a = False
            tls_report_df = pd.read_csv(inject_dir + "a_tls_report.csv", float_precision='round_trip', sep=',',
                                        usecols=['period', 'radius', 'epoch', 'found', 'snr', 'sde', 'run'])
            samples_analysed = sherlock_samples
            for index, row in tls_report_df[::-1].iterrows():
                file = os.path.join(
                    'P' + str(row['period']) + '_R' + str(row['radius']) + '_' + str(row['epoch']) + '.csv')
                first_false = index > 0 and tls_report_df.iloc[index - 1]['found'] and \
                            not tls_report_df.iloc[index]['found']
                if first_false:
                    samples_analysed = 0
                elif tls_report_df.iloc[index]['found']:
                    samples_analysed = sherlock_samples
                if samples_analysed < sherlock_samples:
                    try:
                        samples_analysed = samples_analysed + 1
                        period = float(re.search("P([0-9]+\\.[0-9]+)", file)[1])
                        r_planet = float(re.search("R([0-9]+\\.[0-9]+)", file)[1])
                        epoch = float(re.search("_([0-9]+\\.[0-9]+)\\.csv", file)[1])
                        signal_selection_algorithm = QuorumSnrBorderCorrectedStopWhenMatchSignalSelector(1, 0, period,
                                                                                                         epoch)
                        df = pd.read_csv(inject_dir + file, float_precision='round_trip', sep=',',
                                         usecols=['#time', 'flux', 'flux_err'])
                        if len(df) == 0:
                            found = True
                            snr = 20
                            sde = 20
                            run = 1
                        else:
                            sherlock.Sherlock(False, object_infos=[MissionInputObjectInfo(self.id, inject_dir + file)]) \
                                .setup_detrend(True, True, 1.5, 4, 12, "biweight", 0.2, 1.0, 20, False,
                                               0.25, "cosine", None) \
                                .setup_transit_adjust_params(5, None, None, 10, None, None, 0.4, 14, 10,
                                                             20, 5, 5.5, 0.05, "mask", "quorum", 1, 0,
                                                             signal_selection_algorithm) \
                                .run()
                            df = pd.read_csv(self.id.replace(" ", "") + "_INP/candidates.csv", float_precision='round_trip', sep=',',
                                             usecols=['curve', 'period', 't0', 'run', 'snr', 'sde', 'rad_p',
                                                      'transits'])
                            snr = df["snr"].iloc[len(df) - 1]
                            run = df["run"].iloc[len(df) - 1]
                            sde = df["sde"].iloc[len(df) - 1]
                            per_run = 0
                            found_period = False
                            j = 0
                            for per in df["period"]:
                                if signal_selection_algorithm.is_harmonic(per, period / 2.):
                                    found_period = True
                                    t0 = df["t0"].iloc[j]
                                    break
                                j = j + 1
                            right_epoch = False
                            if found_period:
                                for i in range(-5, 5):
                                    right_epoch = right_epoch or (np.abs(t0 - epoch + i * period) < (
                                            1. / 24.))
                                    if right_epoch:
                                        snr = df["snr"].iloc[j]
                                        run = df["run"].iloc[j]
                                        sde = df["sde"].iloc[j]
                                        break
                            found = right_epoch
                        new_report = {"period": period, "radius": r_planet, "epoch": epoch, "found": found, "sde": sde,
                                      "snr": snr,
                                      "run": int(run)}
                        reports_df = reports_df.append(new_report, ignore_index=True)
                        reports_df.to_csv(inject_dir + "a_sherlock_report.csv", index=False)
                        print("P=" + str(period) + ", R=" + str(r_planet) + ", T0=" + str(epoch) + ", FOUND WAS " + str(
                            found) +
                              " WITH SNR " + str(snr) + "and SDE " + str(sde))
                    except Exception as e:
                        print(e)
                        print("File not valid: " + file)


    def __make_model(self, time, flux, flux_err, rstar, mstar, epoch, period, rplanet):
        # a = (7.495e-6 * period**2)**(1./3.)*u.au #in AU
        P1 = period * u.day
        a = np.cbrt((ac.G * mstar * P1 ** 2) / (4 * np.pi ** 2)).to(u.au)
        # print("radius_1 =", rstar.to(u.au) / a) #star radius convert from AU to in units of a
        # print("radius_2 =", rplanet.to(u.au) / a)
        texpo = 2. / 60. / 24.
        # print("T_expo = ", texpo,"dy")
        # tdur=t14(R_s=radius, M_s=mass,P=period,small_planet=False) #we define the typical duration of a small planet in this star
        # print("transit_duration= ", tdur*24*60,"min" )
        model = ellc.lc(
            t_obs=time,
            radius_1=rstar.to(u.au) / a,  # star radius convert from AU to in units of a
            radius_2=rplanet.to(u.au) / a,  # convert from Rearth (equatorial) into AU and then into units of a
            sbratio=0,
            incl=90,
            light_3=0,
            t_zero=epoch,
            period=period,
            a=None,
            q=1e-6,
            f_c=None, f_s=None,
            ldc_1=self.ab, ldc_2=None,
            gdc_1=None, gdc_2=None,
            didt=None,
            domdt=None,
            rotfac_1=1, rotfac_2=1,
            hf_1=1.5, hf_2=1.5,
            bfac_1=None, bfac_2=None,
            heat_1=None, heat_2=None,
            lambda_1=None, lambda_2=None,
            vsini_1=None, vsini_2=None,
            t_exp=texpo, n_int=None,
            grid_1='default', grid_2='default',
            ld_1='quad', ld_2=None,
            shape_1='sphere', shape_2='sphere',
            spots_1=None, spots_2=None,
            exact_grav=False, verbose=1)
        flux_t = flux + model - 1.
        if model[0] > 0:
            result_flux = flux_t
            result_flux_err = flux_err
            result_time = time
        else:
            result_flux = []
            result_time = []
            result_flux_err = []
        return result_time, result_flux, result_flux_err

    def __transit_masks(self, transit_masks, time):
        result = np.full(len(time), False)
        for mask in transit_masks:
            intransit = transit_mask(time, mask["P"], 2 * mask["D"], mask["T0"])
            result[intransit] = True
        return result

    def __tls_search(self, time, flux, rstar, rstar_min, rstar_max, mass, mstar_min, mstar_max, ab, intransit, epoch,
                     period, min_period, max_period, min_snr, cores, transit_template):
        SNR = 1e12
        FOUND_SIGNAL = False
        time = time[~intransit]
        flux = flux[~intransit]
        time, flux = cleaned_array(time, flux)
        run = 0
        #TODO allow addition of custom window length
        flux = wotan.flatten(time, flux, window_length=0.5, return_trend=False, method='biweight', break_tolerance=0.5)
        #::: search for the rest
        while (SNR >= min_snr) and (not FOUND_SIGNAL):
            model = transitleastsquares(time, flux)
            # R_starx = rstar / u.R_sun
            results = model.power(u=ab,
                                  R_star=rstar,  # rstar/u.R_sun,
                                  R_star_min=rstar_min,  # rstar_min/u.R_sun,
                                  R_star_max=rstar_max,  # rstar_max/u.R_sun,
                                  M_star=mass,  # mstar/u.M_sun,
                                  M_star_min=mstar_min,  # mstar_min/u.M_sun,
                                  M_star_max=mstar_max,  # mstar_max/u.M_sun,
                                  period_min=min_period,
                                  period_max=max_period,
                                  n_transits_min=2,
                                  show_progress_bar=False,
                                  use_threads=cores,
                                  transit_template=transit_template
                                  )
            SNR = results.snr
            if results.snr >= min_snr:
                intransit_result = transit_mask(time, results.period, 2 * results.duration, results.T0)
                time = time[~intransit_result]
                flux = flux[~intransit_result]
                time, flux = cleaned_array(time, flux)
                right_period = self.__is_multiple_of(results.period, period / 2.)
                right_epoch = False
                for tt in results.transit_times:
                    for i in range(-5, 5):
                        right_epoch = right_epoch or (np.abs(tt - epoch + i * period) < (
                                1. / 24.))  # check if any epochs matches to within 1 hour
                #            right_depth   = (np.abs(np.sqrt(1.-results.depth)*rstar - rplanet)/rplanet < 0.05) #check if the depth matches
                if right_period and right_epoch:
                    FOUND_SIGNAL = True
                    break
            run = run + 1
        return FOUND_SIGNAL, results.snr, results.SDE, run

    def __equal(self, a, b, tolerance=0.01):
        return np.abs(a - b) < tolerance

    def __is_multiple_of(self, a, b, tolerance=0.05):
        a = np.float(a)
        b = np.float(b)
        mod_ab = a % b
        mod_ba = b % a
        return (a > b and a < b * 3 + tolerance * 3 and (
                    abs(mod_ab % 1) <= tolerance or abs((b - mod_ab) % 1) <= tolerance)) or \
               (b > a and a > b / 3 - tolerance / 3 and (
                           abs(mod_ba % 1) <= tolerance or abs((a - mod_ba) % 1) <= tolerance))


class QuorumSnrBorderCorrectedStopWhenMatchSignalSelector(QuorumSnrBorderCorrectedSignalSelector):
    def __init__(self, strength=1, min_quorum=0, per=None, t0=None):
        super().__init__()
        self.strength = strength
        self.min_quorum = min_quorum
        self.per = per
        self.t0 = t0

    def select(self, transit_results, snr_min, detrend_method, wl):
        signal_selection = super(QuorumSnrBorderCorrectedStopWhenMatchSignalSelector, self) \
            .select(transit_results, snr_min, detrend_method, wl)
        if signal_selection.score == 0 or (
                self.is_harmonic(signal_selection.transit_result.period, self.per) and
                self.isRightEpoch(signal_selection.transit_result.t0, self.t0, self.per)):
            signal_selection.score = 0
        return signal_selection

    def is_harmonic(self, a, b, tolerance=0.05):
        a = np.float(a)
        b = np.float(b)
        mod_ab = a % b
        mod_ba = b % a
        return (a > b and a < b * 3 + tolerance * 3 and (
                    abs(mod_ab % 1) <= tolerance or abs((b - mod_ab) % 1) <= tolerance)) or \
               (b > a and a > b / 3 - tolerance / 3 and (
                           abs(mod_ba % 1) <= tolerance or abs((a - mod_ba) % 1) <= tolerance))

    def isRightEpoch(self, t0, known_epoch, known_period):
        right_epoch = False
        for i in range(-5, 5):
            right_epoch = right_epoch or (np.abs(t0 - known_epoch + i * known_period) < (
                    1. / 24.))
        return right_epoch

if __name__ == '__main__':
    current_path = os.path.dirname(os.path.realpath(__file__))
    ap = ArgumentParser(description='Sherlock Inject&Recovery tool')
    ap.add_argument('--dir', default=current_path, help="Working directory (if empty your current dir will be assumed)",
                    required=False)
    ap.add_argument('--target', type=str, help="The Kepler/K2/TESS target to be used.", required=True)
    ap.add_argument('--sectors', type=str, default='all', help="The sectors to be used.", required=False)
    ap.add_argument('--min_period', type=float, help="The min period for the period grid", required=True)
    ap.add_argument('--max_period', type=float, help="The max period for the period grid", required=True)
    ap.add_argument('--step_period', type=float, help="The period grid difference between each adjacent value",
                    required=True)
    ap.add_argument('--min_radius', type=float, help="The min planet radius of the injection grid", required=True)
    ap.add_argument('--max_radius', type=float, help="The max planet radius of the injection grid", required=True)
    ap.add_argument('--step_radius', type=float, help="The radius grid difference between each adjacent value",
                    required=True)
    ap.add_argument('--phases', type=int, default=5, help="Number of T0s to be explored for each period and radius.",
                    required=True)
    ap.add_argument('--sherlock_deepness', type=int, default=0, help="Number of steps to be explored with Sherlock "
                                                                     "(default 0).", required=False)
    ap.add_argument('--cpus', type=int, help="The number of CPU cores to be used.", required=True)
    args = ap.parse_args()
    ir = TIRMA(args.target, [int(i) for i in args.sectors.replace(" ", "").split(",")], args.dir) \
        .recovery(args.cpus, args.sherlock_deepness)
    # .inject(args.phases, args.min_period, args.max_period, args.step_period, args.min_radius, args.max_radius,
    #         args.step_radius)\