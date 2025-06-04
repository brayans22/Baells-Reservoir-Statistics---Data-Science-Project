# Author: Brayan Saiago
# Test for exercise 1

# Import libraries
import unittest
import pandas as pd
from src import exercise1


class TestExercise1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Loading dataset")
        cls._df = exercise1.load_dataset("data/aigua.csv")

    def test_expected_columns(self):
        print("Running test_expected_columns")
        expected = [
            "Dia",
            "Estació",
            "Nivell absolut (msnm)",
            "Percentatge volum embassat (%)",
            "Volum embassat (hm3)"
        ]
        for col in expected:
            self.assertIn(col, self._df.columns)

    def test_type_is_dataframe(self):
        print("Running test_type_is_dataframe")
        self.assertIsInstance(self._df, pd.DataFrame)

    def test_dataset_not_empty(self):
        print("Running test_dataset_not_empty")
        self.assertFalse(self._df.empty)

    def test_first_row_values(self):
        print("Running test_first_row_values")
        row = self._df.iloc[0]

        self.assertEqual(row["Dia"], "02/06/2025")
        self.assertEqual(row["Estació"], "Embassament de Riudecanyes")
        self.assertEqual(row["Nivell absolut (msnm)"], 213.66)
        self.assertEqual(row["Percentatge volum embassat (%)"], 61.1)
        self.assertEqual(row["Volum embassat (hm3)"], 3.25)


if __name__ == "__main__":
    unittest.main()
