# check_csv_problems.py
# This script checks a CSV file for common data problems.
# It uses the pandas library to identify missing values,
# duplicated rows, and incorrect data types.

import pandas as pd

# Load the CSV file
df = pd.read_csv("data.csv")

print("CSV DATA CHECK")
print("------------------")

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Check for duplicate rows
duplicates = df.duplicated().sum()
print("\nNumber of duplicate rows:", duplicates)

# Display data types of each column
print("\nColumn data types:")
print(df.dtypes)

# Display general information about the dataset
print("\nDataset information:")
print(df.info())
