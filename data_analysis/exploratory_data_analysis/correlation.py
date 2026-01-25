import pandas as pd
import numpy as np
from scipy import stats

# Define column headers for the automobile dataset
headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
           "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight",
           "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio",
           "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]

# Load the dataset with custom headers
df = pd.read_csv("imports-85.data", names=headers)

# Replace '?' with NaN values
df.replace('?', np.nan, inplace = True)

print(df[["horsepower", "price"]].describe())

# Pearson Correlation between horsepower and price

# Convert horsepower and price to numeric
df["horsepower"] = pd.to_numeric(df["horsepower"])
df["price"] = pd.to_numeric(df["price"])
# Drop rows with NaN values in horsepower or price
df.dropna(subset=["horsepower", "price"], inplace=True)

pearson_coef, p_value = stats.pearsonr(df["horsepower"], df["price"])

print(f"Pearson Correlation Coefficient between horsepower and price: {pearson_coef}, with a P-value of: {p_value}")