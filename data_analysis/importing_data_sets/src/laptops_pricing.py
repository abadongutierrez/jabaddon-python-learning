import pandas as pd
import numpy as np

file_path = './laptop_pricing_dataset_base.csv'

df = pd.read_csv(file_path)
print(df.head())

headers = ["Manufacturer", "Category", "Screen", "GPU", "OS", "CPU_core", "Screen_Size_inch", "CPU_frequency", "RAM_GB", "Storage_GB_SSD", "Weight_kg", "Price"]
df.columns = headers

print(df.head())

# Replace '?' with NaN values
df.replace('?',np.nan, inplace = True)

# Print the data types of each column
print(df.dtypes)

# Get a statistical summary of the DataFrame 
print(df.describe(include='all'))