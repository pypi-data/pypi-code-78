"""Module for time series utilities with a focus on pandas compatibility."""

from typing import Any, Dict, List, Optional, Union

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils.validation import check_is_fitted


class SimpleTimeFeatures(BaseEstimator, TransformerMixin):
    """
    Enrich pandas dataframes with new columns which are easy derivations from its DatetimeIndex, such as the day of week or the month.

    Parameters
    ----------
    second : bool, default=False
        Whether to extract the day of week from the index and add it as a new column.

    minute : bool, default=False
        Whether to extract the day of week from the index and add it as a new column.

    hour : bool, default=False
        Whether to extract the day of week from the index and add it as a new column.

    day_of_week : bool, default=False
        Whether to extract the day of week from the index and add it as a new column.

    day_of_month : bool, default=False
        Whether to extract the day of month from the index and add it as a new column.

    day_of_year : bool, default=False
        Whether to extract the day of year from the index and add it as a new column.

    week_of_month : bool, default=False
        Whether to extract the week of month from the index and add it as a new column.

    week_of_year : bool, default=False
        Whether to extract the week of year from the index and add it as a new column.

    month : bool, default=False
        Whether to extract the month from the index and add it as a new column.

    year : bool, default=False
        Whether to extract the year from the index and add it as a new column.

    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame(
    ...     {"A": ["a", "b", "c"]},
    ...     index=[
    ...         pd.Timestamp("1988-08-08"),
    ...         pd.Timestamp("2000-01-01"),
    ...         pd.Timestamp("1950-12-31"),
    ...     ])
    >>> SimpleTimeFeatures(day_of_month=True, month=True, year=True).fit_transform(df)
                A  day_of_month  month  year
    1988-08-08  a             8      8  1988
    2000-01-01  b             1      1  2000
    1950-12-31  c            31     12  1950
    """

    def __init__(
        self,
        second: bool = False,
        minute: bool = False,
        hour: bool = False,
        day_of_week: bool = False,
        day_of_month: bool = False,
        day_of_year: bool = False,
        week_of_month: bool = False,
        week_of_year: bool = False,
        month: bool = False,
        year: bool = False,
    ) -> None:
        """Initialize."""
        self.second = second
        self.minute = minute
        self.hour = hour
        self.day_of_week = day_of_week
        self.day_of_month = day_of_month
        self.day_of_year = day_of_year
        self.week_of_month = week_of_month
        self.week_of_year = week_of_year
        self.month = month
        self.year = year

    def _add_second(self, X: pd.DataFrame) -> pd.DataFrame:
        return X.assign(second=lambda df: df.index.second) if self.second else X

    def _add_minute(self, X: pd.DataFrame) -> pd.DataFrame:
        return X.assign(minute=lambda df: df.index.minute) if self.minute else X

    def _add_hour(self, X: pd.DataFrame) -> pd.DataFrame:
        return X.assign(hour=lambda df: df.index.hour) if self.hour else X

    def _add_day_of_week(self, X: pd.DataFrame) -> pd.DataFrame:
        return (
            X.assign(day_of_week=lambda df: df.index.weekday + 1)
            if self.day_of_week
            else X
        )

    def _add_day_of_month(self, X: pd.DataFrame) -> pd.DataFrame:
        return (
            X.assign(day_of_month=lambda df: df.index.day) if self.day_of_month else X
        )

    def _add_day_of_year(self, X: pd.DataFrame) -> pd.DataFrame:
        return (
            X.assign(day_of_year=lambda df: df.index.dayofyear)
            if self.day_of_year
            else X
        )

    def _add_week_of_month(self, X: pd.DataFrame) -> pd.DataFrame:
        return (
            X.assign(week_of_month=lambda df: np.ceil(df.index.day / 7).astype(int))
            if self.week_of_month
            else X
        )

    def _add_week_of_year(self, X: pd.DataFrame) -> pd.DataFrame:
        return (
            X.assign(week_of_year=lambda df: df.index.isocalendar().week)
            if self.week_of_year
            else X
        )

    def _add_month(self, X: pd.DataFrame) -> pd.DataFrame:
        return X.assign(month=lambda df: df.index.month) if self.month else X

    def _add_year(self, X: pd.DataFrame) -> pd.DataFrame:
        return X.assign(year=lambda df: df.index.year) if self.year else X

    def fit(self, X: pd.DataFrame, y: Any = None) -> "SimpleTimeFeatures":
        """
        Fit the estimator.

        In this special case, nothing is done.

        Parameters
        ----------
        X : Ignored
            Not used, present here for API consistency by convention.

        y : Ignored
            Not used, present here for API consistency by convention.

        Returns
        -------
        SimpleTimeFeatures
            Fitted transformer.
        """
        self.fitted_ = True
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        """
        Insert all chosen time features as new columns into the dataframe and output it.

        Parameters
        ----------
        X : pd.DataFrame
            A pandas dataframe with a DatetimeIndex.

        Returns
        -------
        pd.DataFrame
            The input dataframe with additional time feature columns.
        """
        check_is_fitted(self)

        res = (
            X.pipe(self._add_second)
            .pipe(self._add_minute)
            .pipe(self._add_hour)
            .pipe(self._add_day_of_week)
            .pipe(self._add_day_of_month)
            .pipe(self._add_day_of_year)
            .pipe(self._add_week_of_month)
            .pipe(self._add_week_of_year)
            .pipe(self._add_month)
            .pipe(self._add_year)
        )
        return res


class PowerTrend(BaseEstimator, TransformerMixin):
    """
    Add a power trend column to a pandas dataframe.

    For example, it can create a new column with numbers increasing quadratically in the index.

    Parameters
    ----------
    power : float, default=1.0
        Exponent to use for the trend, i.e. linear (power=1.), root (power=0.5), or cube (power=3.).

    frequency : Optional[str], default=None
        A pandas time frequency. Can take values like "d" for day or "m" for month. A full list can
        be found on https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-offset-aliases.
        If None, the transformer tries to infer it during fit time.

    origin_date : Optional[Union[str, pd.Timestamp]], default=None
        A date the trend originates from, i.e. the value of the trend column is zero for this date.
        If None, the transformer uses the smallest date of the training set during fit time.

    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame(
    ...     {"A": ["a", "b", "c", "d"]},
    ...     index=pd.date_range(start="1988-08-08", periods=4)
    ... )
    >>> PowerTrend(power=2., frequency="d", origin_date="1988-08-06").fit_transform(df)
                A  trend
    1988-08-08  a    4.0
    1988-08-09  b    9.0
    1988-08-10  c   16.0
    1988-08-11  d   25.0
    """

    def __init__(
        self,
        power: float = 1.0,
        frequency: Optional[str] = None,
        origin_date: Optional[Union[str, pd.Timestamp]] = None,
    ) -> None:
        """Initialize."""
        self.power = power
        self.frequency = frequency
        self.origin_date = origin_date

    def fit(self, X: pd.DataFrame, y: None = None) -> "PowerTrend":
        """
        Fit the model.

        The point of origin and the frequency is constructed here, if not provided during initialization.

        Parameters
        ----------
        X : pd.DataFrame
            Used for inferring the frequency and the origin date, if not provided during initialization.

        y : Ignored
            Not used, present here for API consistency by convention.

        Returns
        -------
        PowerTrend
            Fitted transformer.

        Raises
        ------
        ValueError
            If no frequency was provided during initialization and also cannot be inferred.
        """
        if self.frequency is None:
            self.freq_ = X.index.freq
            if self.freq_ is None:
                raise ValueError(
                    "No frequency provided. It was also impossible to infer it while fitting. Please provide a value in the frequency keyword."
                )
        else:
            self.freq_ = pd.tseries.frequencies.to_offset(self.frequency)

        if self.origin_date is None:
            self.origin_ = X.index.min()
        else:
            self.origin_ = pd.Timestamp(self.origin_date, freq=self.freq_)

        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        """
        Add the trend column to the input dataframe.

        Parameters
        ----------
        X : pd.DataFrame
             A pandas dataframe with a DatetimeIndex.

        Returns
        -------
        pd.DataFrame
            The input dataframe with an additional trend column.

        """
        check_is_fitted(self)

        extended_index = pd.date_range(
            start=self.origin_, end=X.index.max(), freq=self.freq_
        )

        dummy_dates = pd.Series(np.arange(len(extended_index)), index=extended_index)

        return X.assign(trend=dummy_dates.reindex(X.index) ** self.power)


class SpecialDayBumps(BaseEstimator, TransformerMixin):
    """
    Enrich a pandas dataframes with a new column that indicate the presense of special days.

    This new column will contain a one for each date specified in the `dates` keyword. The other entries
    of the column can

    - be zero, yielding a one hot encoded column for these dates, or
    - flatten when going further away from the date in a bell-shaped curve fashion.

    Parameters
    ----------
    name : str
        The name of the new column. Usually a holiday name such as Easter, Christmas, Black Friday, ...

    dates : List[Union[pd.Timestamp, str]]
        A list containing the dates of the holiday. You have to state every holiday explicitly, i.e.
        Christmas from 2018 to 2020 can be encoded as ["2018-12-24", "2019-12-24", "2020-12-24"].

    frequency : Optional[str], default=None
        A pandas time frequency. Can take values like "d" for day or "m" for month. A full list can
        be found on https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-offset-aliases.
        If None, the transformer tries to infer it during fit time.

    window : int, default=1
        Size of the sliding window. The effect of a holiday will reach from approximately
        date - `window/2 * frequency` to date + `window/2 * frequency`, i.e. it is centered around the dates in `dates`.

    p : float, default=1
        Parameter for the shape of the curve. p=1 yields a typical Gaussian curve while p=0.5 yields a Laplace curve, for example.

    sig : float, default=1
        Parameter for the standard deviation of the bell-shaped curve.

    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({"A": range(7)}, index=pd.date_range(start="2019-12-29", periods=7))
    >>> SpecialDayBumps("new_year_2020", ["2020-01-01"]).fit_transform(df)
                A  new_year_2020
    2019-12-29  0            0.0
    2019-12-30  1            0.0
    2019-12-31  2            0.0
    2020-01-01  3            1.0
    2020-01-02  4            0.0
    2020-01-03  5            0.0
    2020-01-04  6            0.0


    >>> SpecialDayBumps("new_year_2020", ["2020-01-01"], frequency="d", window=5, p=1, sig=1).fit_transform(df)
                A  new_year_2020
    2019-12-29  0       0.000000
    2019-12-30  1       0.135335
    2019-12-31  2       0.606531
    2020-01-01  3       1.000000
    2020-01-02  4       0.606531
    2020-01-03  5       0.135335
    2020-01-04  6       0.000000

    """

    def __init__(
        self,
        name: str,
        dates: List[Union[pd.Timestamp, str]],
        frequency: Optional[str] = None,
        window: int = 1,
        p: float = 1,
        sig: float = 1,
    ) -> None:
        """Initialize."""
        self.name = name
        self.dates = dates
        self.frequency = frequency
        self.window = window
        self.p = p
        self.sig = sig

    def fit(self, X: pd.DataFrame, y: None = None) -> "SpecialDayBumps":
        """
        Fit the estimator.

        Creates a pandas offset object.

        Parameters
        ----------
        X : pd.DataFrame
            Used for inferring the frequency, if not provided during initialization.

        y : Ignored
            Not used, present here for API consistency by convention.

        Returns
        -------
        SpecialDayBumps
            Fitted transformer.

        Raises
        ------
        ValueError
            If no frequency was provided during initialization and also cannot be inferred.

        """
        if self.frequency is None:
            self.freq_ = X.index.freq
            if self.freq_ is None:
                raise ValueError(
                    "No frequency provided. It was also impossible to infer it while fitting. Please provide a value in the frequency keyword."
                )
        else:
            self.freq_ = pd.tseries.frequencies.to_offset(self.frequency)

        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        """
        Add the new date feature to the dataframe.

        Parameters
        ----------
        X : pd.DataFrame
            A pandas dataframe with a DatetimeIndex.

        Returns
        -------
        pd.DataFrame
            The input dataframe with an additional column for special dates.
        """
        check_is_fitted(self)

        extended_index = pd.date_range(
            start=X.index.min() - self.window * self.freq_,
            end=X.index.max() + self.window * self.freq_,
            freq=self.freq_,
        )

        dummy_dates = pd.Series(extended_index.isin(self.dates), index=extended_index)

        smoothed_dates = (
            dummy_dates.rolling(
                window=self.window, center=True, win_type="general_gaussian"
            )
            .sum(p=self.p, sig=self.sig)
            .reindex(X.index)
            .values
        )

        return X.assign(**{self.name: smoothed_dates})


class CyclicalEncoder(BaseEstimator, TransformerMixin):
    """
    Break each cyclic feature into two new features, corresponding to the representation of this feature on a circle.

    For example, take the hours from 0 to 23. On a normal, round  analog clock,
    these features are perfectly aligned on a circle already. You can do the same with days, month, ...

    The column names affected by default are

        - second
        - minute
        - hour
        - day_of_week
        - day_of_month
        - day_of_year
        - week_of_month
        - week_of_year
        - month

    You can add more with the additional_cycles parameter.

    Notes
    -----
    This method has the advantage that close points in time stay close together. See the examples below.

    Otherwise, if algorithms deal with the raw value for hour they cannot know that 0 and 23 are actually close.
    Another possibility is one hot encoding the hour. This has the disadvantage that it breaks the distances
    between different hours. Hour 5 and 16 have the same distance as hour 0 and 23 when doing this.

    Parameters
    ----------
    additional_cycles : Optional[Dict[str, Dict[str, int]]], default=None
        Define additional additional_cycles in the form {cycle_name: {"min": min_value, "max": max_value}}, e.g.
        {"day_of_week": {"min": 1, "max": 7}}. Probably you need this only for very specific additional_cycles, as
        these ones are already implemented:

            - "second": {"min": 0, "max": 59},
            - "minute": {"min": 0, "max": 59},
            - "hour": {"min": 0, "max": 23},
            - "day_of_week": {"min": 1, "max": 7},
            - "day_of_month": {"min": 1, "max": 31},
            - "day_of_year": {"min": 1, "max": 366},
            - "week_of_month": {"min": 1, "max": 5},
            - "week_of_year": {"min": 1, "max": 53},
            - "month": {"min": 1, "max": 12}

    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({"hour": [22, 23, 0, 1, 2]})
    >>> CyclicalEncoder().fit_transform(df)
       hour  hour_cos  hour_sin
    0    22  0.866025 -0.500000
    1    23  0.965926 -0.258819
    2     0  1.000000  0.000000
    3     1  0.965926  0.258819
    4     2  0.866025  0.500000
    """

    def __init__(
        self, additional_cycles: Optional[Dict[str, Dict[str, int]]] = None
    ) -> None:
        """Initialize."""
        DEFAULT_CYCLES = {
            "second": {"min": 0, "max": 59},
            "minute": {"min": 0, "max": 59},
            "hour": {"min": 0, "max": 23},
            "day_of_week": {"min": 1, "max": 7},
            "day_of_month": {"min": 1, "max": 31},
            "day_of_year": {"min": 1, "max": 366},
            "week_of_month": {"min": 1, "max": 5},
            "week_of_year": {"min": 1, "max": 53},
            "month": {"min": 1, "max": 12},
        }
        self.additional_cycles = additional_cycles
        if additional_cycles is not None:
            self.additional_cycles.update(DEFAULT_CYCLES)
        else:
            self.additional_cycles = DEFAULT_CYCLES

    def fit(self, X: pd.DataFrame, y=None) -> "CyclicalEncoder":
        """
        Fit the estimator. In this special case, nothing is done.

        Parameters
        ----------
        X : Ignored
            Not used, present here for API consistency by convention.

        y : Ignored
            Not used, present here for API consistency by convention.

        Returns
        -------
        CyclicalEncoder
            Fitted transformer.
        """
        self.fitted_ = True
        return self

    def transform(self, X):
        """
        Add the cyclic features to the dataframe.

        Parameters
        ----------
        X : pd.DataFrame
            A pandas dataframe. The column names should be key in the `additional_cycles` keyword in this class
            or some of

                - "second"
                - "minute"
                - "hour"
                - "day_of_week"
                - "day_of_month"
                - "day_of_year"
                - "week_of_month"
                - "week_of_year"
                - "month"

        Returns
        -------
        pd.DataFrame
            The input dataframe with two additional columns for each original column.
        """
        check_is_fitted(self)

        def min_max(col):
            return (
                (X[col] - self.additional_cycles[col]["min"])
                / (
                    self.additional_cycles[col]["max"]
                    + 1
                    - self.additional_cycles[col]["min"]
                )
                * 2
                * np.pi
            )

        return X.assign(
            **{
                f"{col}_cos": np.cos(min_max(col))
                for col in X.columns.intersection(self.additional_cycles.keys())
            },
            **{
                f"{col}_sin": np.sin(min_max(col))
                for col in X.columns.intersection(self.additional_cycles.keys())
            },
        )
