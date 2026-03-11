# csv_statistics.py
# This script calculates statistics for numeric columns
# in a CSV file using pandas.

import pandas as pd

# Load the CSV file
df = pd.read_csv("data.csv")

print("DATA STATISTICS")
print("------------------")

# Select only numeric columns
numeric_df = df.select_dtypes(include=['number'])

# Calculate statistics
print("\nMaximum values:")
print(numeric_df.max())

print("\nMinimum values:")
print(numeric_df.min())

print("\nAverage values:")
print(numeric_df.mean())
