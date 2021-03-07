# -*- coding: utf-8 -*-


# PyMeeus: Python module implementing astronomical algorithms.
# Copyright (C) 2018  Dagoberto Salazar
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from pymeeus.base import TOL
from pymeeus.Moon import Moon
from pymeeus.Epoch import Epoch


# Moon class

def test_moon_geocentric_ecliptical_pos():
    """Tests the method 'geocentric_ecliptical_pos()' of Moon class"""

    epoch = Epoch(1992, 4, 12.0)
    Lambda, Beta, Delta, ppi = Moon.geocentric_ecliptical_pos(epoch)
    Lambda = round(Lambda, 6)
    Beta = round(Beta, 6)
    Delta = round(Delta, 1)
    ppi = round(ppi, 6)

    assert abs(Lambda - 133.162655) < TOL, \
        "ERROR: 1st 'geocentric_ecliptical_pos()' test, 'Lambda' value doesn't\
            match"

    assert abs(Beta - (-3.229126)) < TOL, \
        "ERROR: 2nd 'geocentric_ecliptical_pos()' test, 'Beta' value doesn't\
            match"

    assert abs(Delta - 368409.7) < TOL, \
        "ERROR: 3rd 'geocentric_ecliptical_pos()' test, 'Delta' value doesn't\
            match"

    assert abs(ppi - 0.991990) < TOL, \
        "ERROR: 4th 'geocentric_ecliptical_pos()' test, 'ppi' value doesn't\
            match"


def test_moon_apparent_ecliptical_pos():
    """Tests the method 'apparent_ecliptical_pos()' of Moon class"""

    epoch = Epoch(1992, 4, 12.0)
    Lambda, Beta, Delta, ppi = Moon.apparent_ecliptical_pos(epoch)
    Lambda = round(Lambda, 5)
    Beta = round(Beta, 6)
    Delta = round(Delta, 1)
    ppi = round(ppi, 6)

    assert abs(Lambda - 133.16726) < TOL, \
        "ERROR: 1st 'apparent_ecliptical_pos()' test, 'Lambda' value doesn't\
            match"

    assert abs(Beta - (-3.229126)) < TOL, \
        "ERROR: 2nd 'apparent_ecliptical_pos()' test, 'Beta' value doesn't\
            match"

    assert abs(Delta - 368409.7) < TOL, \
        "ERROR: 3rd 'apparent_ecliptical_pos()' test, 'Delta' value doesn't\
            match"

    assert abs(ppi - 0.991990) < TOL, \
        "ERROR: 4th 'apparent_ecliptical_pos()' test, 'ppi' value doesn't\
            match"


def test_moon_apparent_equatorial_pos():
    """Tests the method 'apparent_equatorial_pos()' of Moon class"""

    epoch = Epoch(1992, 4, 12.0)
    ra, dec, Delta, ppi = Moon.apparent_equatorial_pos(epoch)
    ra = round(ra, 6)
    dec = round(dec, 6)
    Delta = round(Delta, 1)
    ppi = round(ppi, 6)

    assert abs(ra - 134.688469) < TOL, \
        "ERROR: 1st 'apparent_equatorial_pos()' test, 'ra' value doesn't\
            match"

    assert abs(dec - 13.768367) < TOL, \
        "ERROR: 2nd 'apparent_equatorial_pos()' test, 'dec' value doesn't\
            match"

    assert abs(Delta - 368409.7) < TOL, \
        "ERROR: 3rd 'apparent_equatorial_pos()' test, 'Delta' value doesn't\
            match"

    assert abs(ppi - 0.991990) < TOL, \
        "ERROR: 4th 'apparent_equatorial_pos()' test, 'ppi' value doesn't\
            match"


def test_moon_longitude_mean_ascending_node():
    """Tests the method 'longitude_mean_ascending_node()' of Moon class"""

    epoch = Epoch(1913, 5, 27.0)
    Omega1 = Moon.longitude_mean_ascending_node(epoch)
    Omega1 = round(Omega1, 1)
    epoch = Epoch(2043, 9, 10.0)
    Omega2 = Moon.longitude_mean_ascending_node(epoch)
    Omega2 = round(Omega2, 1)
    epoch = Epoch(1959, 12, 7.0)
    Omega3 = Moon.longitude_mean_ascending_node(epoch)
    Omega3 = round(Omega3, 1)
    epoch = Epoch(2108, 11, 3.0)
    Omega4 = Moon.longitude_mean_ascending_node(epoch)
    Omega4 = round(Omega4, 1)

    assert abs(Omega1 - 0.0) < TOL, \
        "ERROR: 1st 'longitude_mean_ascending_node()' test, 'Omega1' value\
            doesn't match"

    assert abs(Omega2 - 0.0) < TOL, \
        "ERROR: 2nd 'longitude_mean_ascending_node()' test, 'Omega2' value\
            doesn't match"

    assert abs(Omega3 - 180.0) < TOL, \
        "ERROR: 3rd 'longitude_mean_ascending_node()' test, 'Omega3' value\
            doesn't match"

    assert abs(Omega4 - 180.0) < TOL, \
        "ERROR: 4th 'longitude_mean_ascending_node()' test, 'Omega4' value\
            doesn't match"


def test_moon_longitude_true_ascending_node():
    """Tests the method 'longitude_true_ascending_node()' of Moon class"""

    epoch = Epoch(1913, 5, 27.0)
    Omega = Moon.longitude_true_ascending_node(epoch)
    Omega = round(Omega, 4)

    assert abs(Omega - 0.8763) < TOL, \
        "ERROR: 1st 'longitude_true_ascending_node()' test, 'Omega' value\
            doesn't match"


def test_moon_longitude_mean_perigee_node():
    """Tests the method 'longitude_mean_perigee()' of Moon class"""

    epoch = Epoch(2021, 3, 5.0)
    Pi = Moon.longitude_mean_perigee(epoch)
    Pi = round(Pi, 5)

    assert abs(Pi - 224.89194) < TOL, \
        "ERROR: 1st 'longitude_mean_perigee()' test, 'Pi' value doesn't match"


def test_moon_illuminated_fraction_disk():
    """Tests the method 'illuminated_fraction_disk()' of Moon class"""

    epoch = Epoch(1992, 4, 12.0)
    k = Moon.illuminated_fraction_disk(epoch)
    k = round(k, 2)

    assert abs(k - 0.68) < TOL, \
        "ERROR: 1st 'illuminated_fraction_disk()' test, 'k' value doesn't\
            match"


def test_moon_position_bright_limb():
    """Tests the method 'position_bright_limb()' of Moon class"""

    epoch = Epoch(1992, 4, 12.0)
    xi = Moon.position_bright_limb(epoch)
    xi = round(xi, 1)

    assert abs(xi - 285.0) < TOL, \
        "ERROR: 1st 'position_bright_limb()' test, 'xi' value doesn't match"


def test_moon_phase():
    """Tests the method 'moon_phase()' of Moon class"""

    epoch = Epoch(1977, 2, 15.0)
    new_moon = Moon.moon_phase(epoch, target="new")
    y, m, d, h, mi, s = new_moon.get_full_date()
    res = (str(y) + "/" + str(m) + "/" + str(d) + " " + str(h) + ":" + str(mi)
           + ":" + str(round(s, 0)))

    assert res == "1977/2/18 3:37:42.0", \
        "ERROR: 1st 'moon_phase()' test, 'res' value doesn't match"

    epoch = Epoch(2044, 1, 15.0)
    new_moon = Moon.moon_phase(epoch, target="last")
    y, m, d, h, mi, s = new_moon.get_full_date()
    res = (str(y) + "/" + str(m) + "/" + str(d) + " " + str(h) + ":" + str(mi)
           + ":" + str(round(s, 0)))

    assert res == "2044/1/21 23:48:17.0", \
        "ERROR: 2nd 'moon_phase()' test, 'res' value doesn't match"


def test_moon_perigee_apogee():
    """Tests the method 'moon_perigee_apogee()' of Moon class"""

    epoch = Epoch(1988, 10, 1.0)
    apogee, parallax = Moon.moon_perigee_apogee(epoch, target="apogee")
    y, m, d, h, mi, s = apogee.get_full_date()
    apo = (str(y) + "/" + str(m) + "/" + str(d) + " " + str(h) + ":" + str(mi))
    para = parallax.dms_str(n_dec=3)

    assert apo == "1988/10/7 20:30", \
        "ERROR: 1st 'moon_perigee_apogee()' test, 'apo' value doesn't match"

    assert para == "54' 0.679''", \
        "ERROR: 2nd 'moon_perigee_apogee()' test, 'para' value doesn't match"
