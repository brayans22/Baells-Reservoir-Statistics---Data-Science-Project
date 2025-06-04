# Author: Brayan Saiago
"""
Exercise 5: Calculate mean and standard deviation thresholds and plot with smoothed signal.
"""

from pandas import DataFrame
import matplotlib.pyplot as plt
from src.exercise4 import run_exercise_4


def add_thresholds(df: DataFrame) -> DataFrame:
    """
    Add upper and lower threshold columns to the DataFrame.

    Args:
        df (DataFrame): DataFrame with 'smoothed' column.

    Returns:
        DataFrame: DataFrame with 'umbral_sup' and 'umbral_inf' columns added.
    """
    df = df.copy()
    mean = df["smoothed"].mean()
    std = df["smoothed"].std()
    df["umbral_sup"] = mean + std
    df["umbral_inf"] = mean - std
    return df


def plot_with_thresholds(df: DataFrame) -> None:
    """
    Plot smoothed signal with upper and lower thresholds.

    Args:
        df (DataFrame): df with 'decimal_date', 'smoothed', 'umbral_sup', 'umbral_inf'.

    Returns:
        None
    """
    plt.figure(figsize=(10, 5))
    plt.plot(df["decimal_date"], df["smoothed"], label="Smoothed", color="blue")
    plt.plot(df["decimal_date"], df["umbral_sup"], label="Upper Threshold", linestyle="--", color="green")
    plt.plot(df["decimal_date"], df["umbral_inf"], label="Lower Threshold", linestyle="--", color="red")
    plt.title("La Baells - Smoothed Signal with Thresholds")
    plt.xlabel("Decimal Date")
    plt.ylabel("Volume (%)")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig("screenshots/la_baells_thresholds.png")
    plt.close()


def run_exercise_5() -> DataFrame:
    """
    Run full pipeline for Exercise 5.

    Returns:
        DataFrame: df with thresholds added.
    """
    df = run_exercise_4()
    df = add_thresholds(df)
    plot_with_thresholds(df)
    return df