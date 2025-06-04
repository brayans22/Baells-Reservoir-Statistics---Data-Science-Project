# Author: Brayan Saiago
# Test for exercise 5

# Import libraries
import unittest
import pandas as pd
import os
from src import exercise5


class TestExercise5(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Running pipeline for exercise 5")
        cls._df = exercise5.run_exercise_5()

    def test_threshold_columns_exist(self):
        print("Running test_threshold_columns_exist")
        self.assertIn("umbral_sup", self._df.columns)
        self.assertIn("umbral_inf", self._df.columns)

    def test_threshold_values_are_correct(self):
        print("Running test_threshold_values_are_correct")
        mean = self._df["smoothed"].mean()
        std = self._df["smoothed"].std()
        self.assertAlmostEqual(self._df["umbral_sup"].iloc[0], mean + std, delta=0.01)
        self.assertAlmostEqual(self._df["umbral_inf"].iloc[0], mean - std, delta=0.01)

    def test_plot_file_generated(self):
        print("Running test_plot_file_generated")
        self.assertTrue(os.path.exists("screenshots/la_baells_thresholds.png"))

    def test_result_not_empty(self):
        print("Running test_result_not_empty")
        self.assertFalse(self._df.empty)


if __name__ == "__main__":
    unittest.main()