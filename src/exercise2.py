# Author: Brayan Saiago
"""
Exercise 2: Clean and filter the dataset to isolate La Baells reservoir.
"""

from pandas import DataFrame
from src.exercise1 import load_dataset


def rename_columns(df: DataFrame) -> DataFrame:
    """
    Rename columns of the df received by parameter.

    Args:
        df (DataFrame): df.

    Returns:
        DataFrame: df with renamed columns.
    """
    new_column_names = {
        "Dia": "dia",
        "Estació": "estacio",
        "Nivell absolut (msnm)": "nivell_msnm",
        "Percentatge volum embassat (%)": "nivell_perc",
        "Volum embassat (hm3)": "volum"
    }
    return df.rename(columns=new_column_names)


def clean_station_names(df: DataFrame) -> DataFrame:
    """
    Remove 'Embassament de' and content in parentheses.

    Args:
        df (DataFrame): df received by parameter.

    Returns:
        DataFrame: df with cleaned station names.
    """

    df["estacio"] = (
        df["estacio"]
        .str.replace(r"Embassament de\s*", "", regex=True)
        .str.replace(r"\s*\(.*?\)", "", regex=True)
        .str.strip()
        .str.title()
    )
    return df


def run_exercise_2() -> DataFrame:
    """
    rename columns, clean names, filter La Baells.

    Returns:
        DataFrame: Filtered DataFrame for La Baells.
    """

    # Load the dataset
    df = load_dataset("data/aigua.csv")

    # Rename columns
    df = rename_columns(df)
    print("Renamed columns:")
    print(df.columns.tolist())

    # Show unique original station names
    print("Original station names:")
    print(df["estacio"].unique())

    # Clean station names
    df = clean_station_names(df)
    print("Cleaned station names:")
    print(df["estacio"].unique())

    # Filter La Baells
    df_labaells = df[df["estacio"] == "La Baells"].copy()
    print("Filtered df La Baells:")
    print(df_labaells.head())

    return df_labaells
