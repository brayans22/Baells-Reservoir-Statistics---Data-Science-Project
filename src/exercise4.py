# Author: Brayan Saiago
"""
Exercise 4: Apply Savitzky-Golay smoothing filter and plot comparison.
"""

from pandas import DataFrame
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
from src.exercise3 import run_exercise_3


def apply_savgol_filter(df: DataFrame, window: int = 31, polyorder: int = 2) -> DataFrame:
    """
    Apply Savitzky-Golay filter to the 'nivell_perc' column.

    Args:
        df (DataFrame): df with 'nivell_perc'.
        window (int): filter window size (must be odd).
        polyorder (int): polynomial order.

    Returns:
        DataFrame: df with an added 'smoothed' column.
    """
    df = df.copy()
    df["smoothed"] = savgol_filter(df["nivell_perc"], window_length=window, polyorder=polyorder)
    return df


def plot_comparison(df: DataFrame) -> None:
    """
    Plot original and smoothed volume percentage data.

    Args:
        df (DataFrame): df with 'decimal_date', 'nivell_perc', and 'smoothed'.

    Returns:
        None
    """
    plt.figure(figsize=(10, 5))
    plt.plot(df["decimal_date"], df["nivell_perc"], label="Original")
    plt.plot(df["decimal_date"], df["smoothed"], label="Smoothed", linestyle="--")
    plt.title("La Baells - Original vs Smoothed Signal")
    plt.xlabel("Decimal Date")
    plt.ylabel("Volume (%)")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig("screenshots/la_baells_smoothed.png")
    plt.close()


def run_exercise_4() -> DataFrame:
    """
        Load processed data, apply smoothing and plot

    Returns:
        DataFrame: df with original and smoothed signal.
    """
    df = run_exercise_3()
    df = apply_savgol_filter(df)
    plot_comparison(df)
    return df