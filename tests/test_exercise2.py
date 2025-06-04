# Author: Brayan Saiago
# Test for exercise 2

# Import libraries
import unittest
import pandas as pd
from src import exercise2, utils


class TestExercise2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Loading dataset")
        cls._df = utils.load_dataset("data/aigua.csv")
        cls._df_renamed = exercise2.rename_columns(cls._df)
        cls._df_cleaned = exercise2.clean_station_names(cls._df_renamed)

    def test_la_baells_is_filtered(self):
        print("Running test_la_baells_is_filtered")
        self.assertFalse(self._df_cleaned[
                             self._df_cleaned["estacio"] == "La Baells"]
                         .empty)

    def test_column_renamed(self):
        print("Running test_column_renamed")
        expected_columns = ["dia", "estacio", "nivell_msnm",
                            "nivell_perc", "volum"]
        self.assertEqual(list(self._df_renamed.columns), expected_columns)

    def test_station_names_are_cleaned(self):
        print("Running test_station_names_are_cleaned")
        stations = self._df_cleaned["estacio"].unique()

        self.assertFalse(any("Embassament de" in name for name in stations))
        self.assertFalse(any("(" in name or ")" in name for name in stations))

    def test_expected_results_run_exercise2(self):
        print("Running test_expected_results_run_exercise2")
        df_exercise2 = exercise2.run_exercise_2()

        # Check type
        self.assertIsInstance(df_exercise2, pd.DataFrame)

        # Check not empty
        self.assertFalse(df_exercise2.empty)

        # Check columns
        expected_columns = ["dia", "estacio", "nivell_msnm",
                            "nivell_perc", "volum"]
        self.assertEqual(list(df_exercise2.columns), expected_columns)

        # Check all rows are La Baells
        unique_stations = df_exercise2["estacio"].unique()
        self.assertEqual(len(unique_stations), 1)
        self.assertEqual(unique_stations[0], "La Baells")


if __name__ == "__main__":
    unittest.main()
