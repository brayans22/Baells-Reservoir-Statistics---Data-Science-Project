# Author: Brayan Saiago
# Test for exercise 3

# Import libraries
import unittest
import pandas as pd
import os
from src import exercise3


class TestExercise3(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Running pipeline for exercise 3")
        cls._df = exercise3.run_exercise_3()

    def test_datetime_column_exists(self):
        print("Running test_datetime_column_exists")
        self.assertIn("datetime", self._df.columns)
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(self._df["datetime"]))

    def test_decimal_date_column_exists(self):
        print("Running test_decimal_date_column_exists")
        self.assertIn("decimal_date", self._df.columns)
        self.assertTrue(pd.api.types.is_float_dtype(self._df["decimal_date"]))

    def test_plot_file_generated(self):
        print("Running test_plot_file_generated")
        self.assertTrue(os.path.exists("screenshots/la_baells_timeseries.png"))

    def test_result_not_empty(self):
        print("Running test_result_not_empty")
        self.assertFalse(self._df.empty)


if __name__ == "__main__":
    unittest.main()