"""
    This file contains the functions to process the dataframe

"""
from typing import Optional
import pandas as pd


def print_rows(dataframe: pd.DataFrame, start: int, end: Optional[int] = None):
    """
    Prints rows from a Dataframe Object.

    Parameters:
    dataframe (pd.Dataframe): The path to the XML file.
    start (int): The index of the start row to print.
    end (int, optional): The index of the end row to print.
    If not specified, only the start row is printed.

    Returns:
    None
    """
    if end is None:  # If no end row is specified, print only the start row
        print(dataframe.iloc[start])
    else:  # If an end row is specified, print all rows from start to end-1
        print(dataframe.iloc[start:end])


def drop_columns(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Drops the specified columns from the given DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame from which columns need to be dropped.
        columns (list): A list of column names to be dropped.

    Returns:
        pd.DataFrame: The DataFrame with the specified columns dropped.
    """
    df = df.drop(columns, axis=1)
    return df
