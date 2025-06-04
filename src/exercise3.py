# Author: Brayan Saiago
"""
Exercise 3: Convert date to datetime and decimal format, plot time series for La Baells.
"""

from pandas import DataFrame
from datetime import datetime
import matplotlib.pyplot as plt
from src.exercise2 import run_exercise_2


def convert_date_column(df: DataFrame) -> DataFrame:
    """
    Convert 'dia' column to datetime format.

    Args:
        df (DataFrame): df received by parameter.

    Returns:
        DataFrame: df with a new 'datetime' column.
    """
    df = df.copy()
    df["datetime"] = df["dia"].apply(lambda x: datetime.strptime(x, "%d/%m/%Y"))
    return df


def to_decimal(dt: datetime) -> float:
    """
    Convert a datetime object to decimal year format.

    Args:
        dt (datetime): datetime object.

    Returns:
        float: decimal representation of the year.
    """
    start = datetime(dt.year, 1, 1)
    year_length = (datetime(dt.year + 1, 1, 1) - start).days
    day_of_year = (dt - start).days
    return dt.year + day_of_year / year_length


def convert_to_decimal_date(df: DataFrame) -> DataFrame:
    """
    Convert 'datetime' column to decimal date (e.g., 2025.42).

    Args:
        df (DataFrame): df with 'datetime' column.

    Returns:
        DataFrame: df with 'decimal_date' column added.
    """
    df = df.copy()
    df["decimal_date"] = df["datetime"].apply(to_decimal)
    return df


def plot_time_series(df: DataFrame) -> None:
    """
    Plot time series of 'nivell_perc' over decimal_date and save to file.

    Args:
        df (DataFrame): df with 'decimal_date' and 'nivell_perc'.

    Returns:
        None
    """
    plt.figure(figsize=(10, 5))
    plt.plot(df["decimal_date"], df["nivell_perc"])
    plt.title("La Baells - Volume Percentage Over Time")
    plt.xlabel("Decimal Date")
    plt.ylabel("Volume (%)")
    plt.grid()
    plt.tight_layout()
    plt.savefig("screenshots/la_baells_timeseries.png")
    plt.close()


def run_exercise_3() -> DataFrame:
    """
    Full pipeline for Exercise 3:
    - Convert date
    - Compute decimal date
    - Plot results

    Returns:
        DataFrame: Processed df with 'datetime' and 'decimal_date'.
    """
    df = run_exercise_2()
    df = convert_date_column(df)
    df = convert_to_decimal_date(df)
    plot_time_series(df)
    return df