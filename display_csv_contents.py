# display_csv_contents.py
# This script reads a CSV file using pandas
# and displays the contents in the console.

import pandas as pd

# Load the CSV file
df = pd.read_csv("data.csv")

print("FULL DATASET")
print("------------------")

# Display the full dataset
print(df)

# Display the first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Display the last 5 rows
print("\nLast 5 rows:")
print(df.tail())
