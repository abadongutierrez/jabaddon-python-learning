import pandas as pd
import numpy as np

# Define column headers for the automobile dataset
headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
           "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight",
           "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio",
           "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]

# Load the dataset with custom headers
df = pd.read_csv("imports-85.data", names=headers)

# Replace '?' with NaN values
df.replace('?', np.nan, inplace = True)

# Convert price column from string to numeric
df["price"] = pd.to_numeric(df["price"])

# Select only the columns needed for analysis
df_selected = df[["drive-wheels", "body-style", "price"]]

print(df_selected.head())

# Group by drive-wheels and body-style, then calculate mean price
# as_index=False to keep group keys as columns
grouped_mean = df_selected.groupby(["drive-wheels", "body-style"], as_index=False).mean()

# Format mean price to 2 decimal places with dollar sign
grouped_mean["f_price"] = grouped_mean["price"].apply(lambda x: f"${x:,.2f}")

print(grouped_mean)

df_pivot = grouped_mean.pivot(index="drive-wheels", columns="body-style", values="f_price")
print(df_pivot)
