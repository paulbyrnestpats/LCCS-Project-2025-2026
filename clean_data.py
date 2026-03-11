# clean_data.py
# This script cleans the CSV dataset by removing rows with missing values
# and filtering unrealistic sensor readings.

import pandas as pd

df = pd.read_csv("data.csv")

# Remove rows with missing values
df = df.dropna()

# Remove unrealistic temperature values
df = df[(df["Temperature"] > -20) & (df["Temperature"] < 60)]

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("Data cleaned and saved to cleaned_data.csv")
