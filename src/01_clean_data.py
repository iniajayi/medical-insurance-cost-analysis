import pandas as pd
import numpy as np
from pathlib import Path

input_path = Path("data/insurance.csv")

output_path = Path ("data/cleaned_insurance.csv")

df = pd.read_csv(input_path)

# Display the first five rows of the original data and its shape (no. of rows and columns) for inspection
print("First 5 rows of the original data:")
print(df.head())        

print("Original data shape:")
print(df.shape)

# Clean column names for consistency and ease of use
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")

)

# Check for missing values in the dataset and display the count of missing values
print("Missing values before cleaning:")
print(df.isnull().sum())

#Creating new column for smoking status based on the 'smoker' column
#Where 'yes' is mapped to 1 and 'no' is mapped to 0
df["smoker_binary"] = np.where(df["smoker"] == "yes", 1, 0)

#Creating BMI categories
df["bmi_category"] = pd.cut(
    df["bmi"], 
    bins=[0, 18.5, 24.9, 29.9, 100],
    labels=["Underweight", "Normal", "Overweight", "Obese"]
)

#Creating age groups in order to compare insurance charges acrosss age bandings
df["age_group"] = pd.cut(
    df["age"],
    bins=[0, 25, 35, 45, 55, 100],
    labels=["18-25", "26-35", "36-45", "46-55", "56+"]
)

df.to_csv(output_path, index=False)

print("Cleaned data saved successfully.")
print("Cleane data shape:")
print(df.shape)

print("First five rows of the cleaned data:")
print(df.head())

