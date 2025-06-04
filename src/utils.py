# Author: Brayan Saiago
"""
Module with utils functions to use in the exercises.
"""

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
