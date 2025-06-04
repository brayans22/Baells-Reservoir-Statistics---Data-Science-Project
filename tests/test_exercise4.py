# Author: Brayan Saiago
# Test for exercise 4

# Import libraries
import unittest
import pandas as pd
import os
from src import exercise4


class TestExercise4(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Running pipeline for exercise 4")
        cls._df = exercise4.run_exercise_4()

    def test_smoothed_column_exists(self):
        print("Running test_smoothed_column_exists")
        self.assertIn("smoothed", self._df.columns)
        self.assertTrue(pd.api.types.is_float_dtype(self._df["smoothed"]))

    def test_smoothed_not_equal_original(self):
        print("Running test_smoothed_not_equal_original")
        self.assertFalse(self._df["smoothed"].equals(self._df["nivell_perc"]))

    def test_plot_file_generated(self):
        print("Running test_plot_file_generated")
        self.assertTrue(os.path.exists("screenshots/la_baells_smoothed.png"))

    def test_result_not_empty(self):
        print("Running test_result_not_empty")
        self.assertFalse(self._df.empty)


if __name__ == "__main__":
    unittest.main()