def config_pandas_display():
    """
    Configure Pandas display
    """
    import pandas as pd

    pd.set_option("display.max_columns", 500)
    # pd.set_option("display.max_colwidth", -1)
    pd.set_option("display.max_colwidth", 500)
    # pd.set_option("display.max_rows", 200)
    pd.set_option("display.expand_frame_repr", True)


def add_type_columns(dataframe):
    """
    Returns Pandas dataframe where each columns has their type column right next to it

    Parameters
    ----------
    dataframe : pandas.DataFrame
        Dataframe to add type columns

    Examples
    --------
    >>> values = [[0, '0', [], {}, None, ""]]
    >>> cols = ["int_", "str_", "list_", "set_", "none_", "_"]
    >>> df = pd.DataFrame(values, columns=cols)
    >>> add_type_columns(df)
       int_      int__type str_      str__type list_      list__type set_       set__type none_          none__type _         __type
    0     0  <class 'int'>    0  <class 'str'>    []  <class 'list'>   {}  <class 'dict'>  None  <class 'NoneType'>    <class 'str'>

    Returns
    -------
    df : pandas.DataFrame
        For each dataframe's column, add a column with it's dtype next to it
    """
    import pandas as pd

    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError("Argument must be a Pandas dataframe ...")

    df = dataframe.copy()
    suffix = "_type"
    for column in df.columns:
        # To prevent creating (1) duplicated column (2) column with ever-increasing suffix [xxx_type, xxx_type_type ...]
        new_col = column + suffix
        if not (new_col in df.columns or column.endswith(suffix)):
            new_col_loc = df.columns.get_loc(column) + 1
            new_col_value = df[column].apply(lambda x: type(x))
            df.insert(new_col_loc, column=new_col, value=new_col_value)
            # df[new_col] = df[column].apply(lambda x: type(x))
    return df


def compare_all_list_items(list_):
    """
    Get dataframe with every combination of 2 list items

    Parameters
    ----------
    list_ : list
        A Python list

    Examples
    --------
    >>> compare_all_list_items([])
    Empty DataFrame
    Columns: [item1, item2, item1_eq_item2]
    Index: []

    >>> compare_all_list_items([1, 1, 2, 3])
      item1 item2  item1_eq_item2
    0     1     1            True
    1     1     2           False
    2     1     3           False
    3     1     2           False
    4     1     3           False
    5     2     3           False

    Returns
    -------
    df : pandas.DataFrame
        Each row represent 1 of all combinations
    """
    import pandas as pd
    from itertools import combinations

    if not isinstance(list_, list):
        raise TypeError("Argument must be a list ...")

    df = []
    for a, b in combinations(list_, 2):
        row = {"item1": repr(a), "item2": repr(b), "item1_eq_item2": a == b}
        df.append(row)

    df = pd.DataFrame(df, columns=["item1", "item2", "item1_eq_item2"])
    return df


def dtypes_dictionary(dataframe):
    """
    Create a dictionary {dtype: [column1, column2 ...]} from Pandas dataframe

    Parameters
    ----------
    dataframe : pandas.DataFrame
        Base dataframe

    Examples
    --------
    >>> dtypes_dictionary(pd.DataFrame())
    Traceback (most recent call last):
      ...
    ValueError: Argument can't be a empty Pandas dataframe ...

    >>> values = [[0, '0', [], {}, None, ""]]
    >>> cols = ["int_", "str_", "list_", "set_", "none_", "_"]
    >>> df = pd.DataFrame(values, columns=cols)
    >>> dtypes_dictionary(df)
    {<class 'numpy.int64'>: ['int_'], <class 'str'>: ['str_', '_'], <class 'list'>: ['list_'], <class 'dict'>: ['set_'], <class 'NoneType'>: ['none_']}

    Returns
    -------
    dict_ : dict
        {str: [column1, column2, ...], int: [column5, ...], ...}
    """
    import pandas as pd

    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError("Argument must be a Pandas dataframe ...")
    if len(dataframe) == 0:
        raise ValueError("Argument can't be a empty Pandas dataframe ...")

    dict_ = {}
    for index, value in dataframe.loc[0].iteritems():
        dtype = type(value)
        if dtype not in dict_:
            dict_[dtype] = [index]
        else:
            dict_[dtype].append(index)

    return dict_


def head_tail(dataframe, n=5):
    """
    Print the Pandas dataframe first n head and last n tail

    Parameters
    ----------
    dataframe : pandas.DataFrame
        Base dataframe
    n : int, optional
        Number of rows

    Examples
    --------
    >>> values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> cols = ["test"]
    >>> df = pd.DataFrame(values, columns=cols)
    >>> head_tail(df)
       test
    0     1
    1     2
    2     3
    3     4
    4     5
    5     6
    6     7
    7     8
    8     9
    9    10

    Returns
    -------
    df : pandas.DataFrame
        A dataframe containing n head and tail of base dataframe
    """
    import pandas as pd

    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError("Argument must be a Pandas dataframe ...")

    df = dataframe.head(n).append(dataframe.tail(n))
    return df


def index_marks(n_rows, chunk_size):
    """
    Determine the range given the
        1. number of rows
        2. desired chunk size

    Parameters
    ----------
    n_rows : int
        The number of rows
    chunk_size : int
        The desire chunk size

    Examples
    --------
    >>> index_marks(10, 3)
    range(3, 12, 3)
    >>> list(index_marks(10, 3))
    [3, 6, 9]

    Returns
    -------
    range_ : range
        Python range
    """
    if not all(isinstance(x, int) for x in [n_rows, chunk_size]):
        raise TypeError("Arguments 1 & 2 must be int ...")

    p1 = 1 * chunk_size
    p2 = (n_rows // chunk_size + 1) * chunk_size
    p3 = chunk_size
    range_ = range(p1, p2, p3)
    return range_


def chunking_dataframe(dataframe, chunk_size):
    """
    Split Pandas dataframe into dataframes with specific chunk_size

    Parameters
    ----------
    dataframe : pandas.DataFrame
        Original dataframe
    chunk_size : int
        The chunk size of each smaller dataframes

    Examples
    --------
    >>> chunking_dataframe(pd.DataFrame(), 2)
    [Empty DataFrame
    Columns: []
    Index: []]

    >>> values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> cols = ["test"]
    >>> df = pd.DataFrame(values, columns=cols)
    >>> chunking_dataframe(df, 5)
    [   test
    0     1
    1     2
    2     3
    3     4
    4     5,    test
    5     6
    6     7
    7     8
    8     9
    9    10, Empty DataFrame
    Columns: [test]
    Index: []]

    >>> chunking_dataframe(df, 4)
    [   test
    0     1
    1     2
    2     3
    3     4,    test
    4     5
    5     6
    6     7
    7     8,    test
    8     9
    9    10]

    Returns
    -------
    list_ : list
        [dataframe, dataframe2, ...]
    """
    import numpy as np
    import pandas as pd

    list_ = None
    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError("Argument must be a Pandas dataframe ...")
    if not isinstance(chunk_size, int):
        raise TypeError("Argument must be a int ...")

    indices = index_marks(dataframe.shape[0], chunk_size)
    list_ = np.split(dataframe, indices)
    return list_


def to_excel_keep_url(filepath, dataframe):
    """
    Save Pandas dataframe as excel, without converting string to urls.
        - Excel auto converts string to urls
        - Excel limit of 65,530 urls per worksheet
        - Excel does not keep url > 255 characters

    Parameters
    ----------
    filepath : str
        Filepath
    dataframe : pandas.DataFrame
        Dataframe to export into excel

    Examples
    --------
    >>> values = ["https://www.shawnngtq.com"]
    >>> cols = ["url"]
    >>> df = pd.DataFrame(values, columns=cols)
    >>> to_excel_keep_url("./tmp.xlsx", df)
    Excel exported ...

    Returns
    -------
    None
        Pandas dataframe => excel with url as url instead of string
    """
    import pandas as pd

    if not isinstance(filepath, str):
        raise TypeError("Argument 1 must be a non-empty string ...")

    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError("Argument 2 must be a Pandas dataframe ...")

    writer = pd.ExcelWriter(filepath, engine="xlsxwriter", options={"strings_to_urls": False})
    dataframe.to_excel(writer, index=False)
    writer.close()
    print("Excel exported ...")


def compare_dataframes(dataframe, dataframe2):
    """
    Compare the before & after Pandas dataframe going through data transformation (DT)

    Parameters
    ----------
    dataframe : pandas.DataFrame
        The Pandas dataframe before DT
    dataframe2 : pandas.DataFrame
        The Pandas dataframe after DT

    Examples
    --------
    >>> df1 = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    >>> df1
       a  b
    0  1  3
    1  2  4
    >>> df2 = df1.copy()
    >>> df2["a"] = df2["a"].apply(lambda x: x*2)
    >>> df2
       a  b
    0  2  3
    1  4  4
    >>> compare_dataframes(df1, df2)
    =======================
    Pandas dataframe length
    =======================
    df1 (input df)  length: 2
    df2 (output df) length: 2
    dataframe length change: True
    <BLANKLINE>
    ----------------
    COMPARE COLUMNS
    ----------------
    df1 non-null a: 2
    df2 non-null a: 2
    df1 & df2 has the same length
    df1 non-null b: 2
    df2 non-null b: 2
    df1 & df2 has the same length

    Returns
    -------
    None
        Print output comparison between 2 Pandas dataframes
    """
    import pandas as pd

    if not all(isinstance(x, pd.DataFrame) for x in [dataframe, dataframe2]):
        raise TypeError("Arguments 1 & 2 must be pandas dataframes ...")

    print("=" * len("Pandas dataframe length"))
    print("Pandas dataframe length")
    print("=" * len("Pandas dataframe length"))
    print(f"df1 (input df)  length: {len(dataframe)}")
    print(f"df2 (output df) length: {len(dataframe)}")
    print(f"dataframe length change: {len(dataframe) == len(dataframe2)}\n")
    print("----------------")
    print("COMPARE COLUMNS")
    print("----------------")
    for column in dataframe.columns:
        pd_df = dataframe[dataframe[column].notnull()]
        pd_df2 = None
        print(f"df1 non-null {column}: {len(pd_df)}")

        try:
            pd_df2 = dataframe2[dataframe2[column].notnull()]
        except KeyError:
            print(f"df2 {column}: does not exist")

        if pd_df2 is not None:
            print(f"df2 non-null {column}: {len(pd_df2)}")

            if len(pd_df) == len(pd_df2):
                print("df1 & df2 has the same length")
            elif len(pd_df2) > len(pd_df):
                print("df2 > df1, check")
            else:
                strings = ["null", "NA"]
                null_count = len(dataframe[dataframe[column].isnull()])
                string_count = len(dataframe[dataframe[column].isin(strings)])
                empty_string_count = len(dataframe[dataframe[column].str.len() == 0])
                non_null_count = len(dataframe) - null_count - string_count - empty_string_count
                print(f"""
                df1 
                - null ({null_count}) 
                - string null ({string_count}) 
                - empty string ({empty_string_count}) 
                = {non_null_count} 
                == df2 ({len(pd_df2)}): {non_null_count == len(pd_df2)}
                """)


def series_count(series):
    """
    Enhanced Pandas series.value_counts()

    Parameters
    ----------
    series : pd.Series
        The series to get value_counts()

    Examples
    --------
    >>> values = [1, 1, 1, 2, 2, 3]
    >>> cols = ["test"]
    >>> df = pd.DataFrame(values, columns=cols)
    >>> series_count(df["test"])
       count    percent
    1      3  50.000000
    2      2  33.333333
    3      1  16.666667

    Returns
    -------
    df : pandas.DataFrame
        Enhanced value_counts() in dataframe
    """
    import pandas as pd

    if not isinstance(series, pd.Series):
        raise TypeError("Argument must be a Pandas series ...")

    df = series.value_counts().to_frame(name="count")
    total = df.sum()["count"]
    df["percent"] = df["count"] / total * 100
    return df


def print_dataframe_overview(dataframe, stats=False):
    """
    Print the value_counts() of each column in dataframe

    Parameters
    ----------
    dataframe : pandas.DataFrame
        Base dataframe
    stats : bool, optional
        Display statistics

    Examples
    --------
    >>> print_dataframe_overview(pd.DataFrame())

    >>> data = {"int_": [1, 1, 2], "str_": ["a", "b", "b"]}
    >>> df = pd.DataFrame(data)
    >>> print_dataframe_overview(df)
    ==============================
    int_
    ==============================
    Unique elements: 2
    Null elements: 0
       count    percent
    1      2  66.666667
    2      1  33.333333
    ==============================
    str_
    ==============================
    Unique elements: 2
    Null elements: 0
       count    percent
    b      2  66.666667
    a      1  33.333333

    Returns
    -------
    None
        Print output in console
    """
    import pandas as pd
    from IPython.display import display

    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError("Argument must be a Pandas dataframe ...")

    for column in dataframe.columns:
        print("=" * 30)
        print(column)
        print("=" * 30)
        try:
            print(f"Unique elements: {dataframe[column].nunique()}")
            print(f"Null elements: {len(dataframe[dataframe[column].isnull()])}")
            if stats:
                print(f"Minimum: {min(dataframe[column])}")
                print(f"Maximum: {max(dataframe[column])}")
            display(series_count(dataframe[column]).head(20))
        except:
            print(f"Unable to get value_counts of {column} ...\n")


def useless_columns(dataframe):
    """
    Return useless columns

    Parameters
    ----------
    dataframe : pandas.DataFrame
        Base dataframe

    Returns
    -------
    empty_columns : list
        List of empty columns
    single_columns : list
        List of single value columns

    (empty_columns, single_columns)
    """
    import pandas as pd

    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError("Argument must be a Pandas dataframe ...")

    empty_columns = dataframe.nunique().where(lambda x: x == 0).dropna().index.values.tolist()
    single_columns = dataframe.nunique().where(lambda x: x == 1).dropna().index.values.tolist()
    print(f"Empty columns: {empty_columns}")
    print(f"Single value columns: {single_columns}")
    return empty_columns, single_columns


def split_left_merged_dataframe(dataframe, dataframe2, columns):
    """
    Split left merged dataframe into dataframes ("both", "left_only")

    Parameters
    ----------
    dataframe : pandas.DataFrame
        Based dataframe
    dataframe2 : pandas.DataFrame
        Dataframe to merged with
    columns : list
        Columns to join on

    Examples
    --------
    >>> df1 = pd.DataFrame({'key': ['foo', 'bar', 'baz', 'foo', "zen"], 'value': [1, 2, 3, 5, 9]})
    >>> df2 = pd.DataFrame({'key': ['foo', 'bar', 'baz', 'foo'], 'value': [5, 6, 7, 8]})
    >>> df_both, df_left = split_left_merged_dataframe(df1, df2, ["key"])
                count    percent
    both            6  85.714286
    left_only       1  14.285714
    right_only      0   0.000000
    >>> df_both
       key  value  value_y _merge
    0  foo      1      5.0   both
    1  foo      1      8.0   both
    2  bar      2      6.0   both
    3  baz      3      7.0   both
    4  foo      5      5.0   both
    5  foo      5      8.0   both
    >>> df_left
       key  value  value_y     _merge
    6  zen      9      NaN  left_only


    Returns
    -------
    df_both : pandas.DataFrame
        Dataframe with merged keys on both input dataframes
    df_left : pandas.DataFrame
        Dataframe whose merge keys only appear in left / base dataframe

    (df_both, df_left)
    """
    import pandas as pd
    from IPython.display import display

    if not all(isinstance(x, pd.DataFrame) for x in [dataframe, dataframe2]):
        raise TypeError("Arguments 1 & 2 must be pandas dataframes ...")
    if not isinstance(columns, list):
        raise TypeError("Argument must be a list ...")

    df_merged = dataframe.merge(dataframe2, on=columns, how="left", indicator=True, suffixes=("", "_y"))
    df_both = df_merged[df_merged["_merge"] == "both"].copy()
    df_left = df_merged[df_merged["_merge"] == "left_only"].copy()
    display(series_count(df_merged["_merge"]))
    return df_both, df_left


def series_to_columns(dataframe, column):
    """
    Convert a pandas dictionary column to pandas column(s)

    Parameters
    ----------
    dataframe : pandas.DataFrame
        Pandas dataframe
    column : pd.Series
        Pandas series with dict dtype

    Examples
    --------
    >>> values = [[1, {'a':1, 'b':2}]]
    >>> cols = ["c1", "c2"]
    >>> df = pd.DataFrame(values, columns=cols)
    >>> df
       c1                c2
    0   1  {'a': 1, 'b': 2}
    >>> series_to_columns(df, "c2")
       c1  a  b
    0   1  1  2

    Returns
    -------
    df : pandas.DataFrame
        A Pandas dataframe with dictionary column converted to column(s)
    """
    import pandas as pd

    df = pd.concat([dataframe.drop([column], axis=1), dataframe[column].apply(pd.Series)], axis=1)
    return df


def clean_none(dataframe):
    """
    Replace None variation to None

    Parameters
    ----------
    dataframe : pandas.DataFrame
        Pandas dataframe

    Examples
    --------
    >>> from data_manipulation.base.base_ import get_none_variation
    >>> df = pd.DataFrame({"c1": get_none_variation()})
    >>> clean_none(df)
          c1
    0   None
    1   None
    2   None
    3   None
    4   None
    5   None
    6   None
    7   None
    8   None
    9   None
    10  None
    11  None
    12  None
    13  None
    14  None
    >>> df = pd.DataFrame({"c1": [""]})
    >>> clean_none(df)
         c1
    0  None
    >>> df = pd.DataFrame({"c1": ["Nathing"]})
    >>> clean_none(df)
            c1
    0  Nathing
    >>> df = pd.DataFrame({"c1": ["Na "]})
    >>> clean_none(df)
        c1
    0  Na

    Returns
    -------
    df : pandas.DataFrame
        A Pandas dataframe with standardized None
    """
    import numpy as np
    import pandas as pd
    from data_manipulation.base.base_ import get_none_variation

    df = dataframe.copy()
    df = df.replace(r"^\s*$", np.nan, regex=True)
    non_variations = get_none_variation()
    df = df.replace(non_variations, np.nan)
    df = df.where(pd.notnull(df), None)
    return df


def split_dataframe(dataframe, uuid, columns):
    """
    Split specific dataframe columns into new dataframe, both dataframes link by uuid

    Parameters
    ----------
    dataframe : pandas.DataFrame
        Original dataframe
    uuid : str
        The uuid that can join the splited dataframes
    columns : list
        The list of columns to split from original dataframe

    Examples
    --------
    >>> df = pd.DataFrame({"a": [1, 2], "b": [2, 3], "uuid": ["abc123", "efg456"]})
    >>> df1, df2 = split_dataframe(df, "uuid", ["b"])
    >>> df1
       a    uuid
    0  1  abc123
    1  2  efg456
    >>> df2
       b    uuid
    0  2  abc123
    1  3  efg456
    >>> df
       a  b    uuid
    0  1  2  abc123
    1  2  3  efg456

    Returns
    -------
    df1: pandas.DataFrame
        Dataframe without the specific columns
    df2: pandas.DataFrame
        Datafrane with specific columns and uuid

    (df1, df2)
    """
    import pandas as pd

    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError("Argument 1 must be pandas.DataFrame ...")
    if not isinstance(uuid, str):
        raise TypeError("Argument 2 must be str ...")
    if not isinstance(columns, list):
        raise TypeError("Argument 3 must be list ...")

    df1 = dataframe[dataframe.columns[~dataframe.columns.isin(columns)]].copy()
    df2 = dataframe[columns + [uuid]].copy()
    return df1, df2


if __name__ == "__main__":
    import doctest
    import pandas as pd

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
