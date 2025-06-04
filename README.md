# Baells-Reservoir-Statistics---Data-Science-Project

This project corresponds to PEC4 of the course Programming for Data Science, part of the UOC's Bachelor's Degree in Data Science.
The main objective of this practical assignment is to apply a complete data analysis pipeline using Python, involving tasks such as data loading, cleaning, transformation, visualization, and signal processing.

## Structure

- `src/`: source code of the project.
- `tests/`: unit tests to test the code.
- `data/`: original data files .csv
- `screenshots/`: images with coverage and test passed correctly
- `doc/`: extended project documentation (README)
- `requirements.txt`: dependencies required for execution.

## Requirements

To run this project, you need to install the requirements using this command:

```bash
pip install -r requirements.txt
```

## How to run

The main file is located in the folder src/, to execute the project you have to run this command:

```bash
python src/main.py
```

## How to run the tests

Tests are located in the `tests/` folder, to run the test you have to execute this commnad:

If you want to execute one test in particular (test_exercise1 in this example):
```bash
python -m unittest tests.test_exercise1
```

## How to run the linter

The project includes linter tools to ensure the code follows the PEP8 style guide.

To run the linter on the entire project, execute the following command:

```bash
flake8 src/ tests/
```

If you want to check a specific file using pylint, for example test_exercise1.py, use:

```bash
pylint tests/test_exercise1.py
```
