# Author: Brayan Saiago
"""
Module for exercise 1
"""

# Import libraries
import pandas as pd
from pandas import DataFrame


def load_dataset(path: str) -> DataFrame:
    """
    Loads a CSV file into a pandas df

    Args:
        path (str): Path to the CSV file.

    Returns:
        DataFrame: The loaded DataFrame.
    """
    return pd.read_csv(path)


def run_exercise_1() -> None:
    """
        Run exercise 1 with the first 5 rows, column names and info.

    Returns:
        None
    """
    # Load the dataset
    df = load_dataset("data/aigua.csv")

    # Display 5 rows
    print("First 5 rows dataset:")
    print(df.head())

    # Display column names
    print("Dataset columns:")
    print(df.columns)

    # Display dataset info
    print("Dataset info:")
    print(df.info())
