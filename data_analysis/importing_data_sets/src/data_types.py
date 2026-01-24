import pandas as pd

url = './automobile/imports-85.data'

# read_csv assume the data has headers if not specified
df = pd.read_csv(url, header=None)

headers = ["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style",
           "drive-wheels","engine-location","wheel-base","length","width","height","curb-weight",
           "engine-type","num-of-cylinders","engine-size","fuel-system","bore","stroke","compression-ratio",
           "horsepower","peak-rpm","city-mpg","highway-mpg","price"]

df.columns = headers

# see column data types
print(df.dtypes)

# get quick statistical summary of the data
print(df.describe())

print(df.describe(include="all"))

# see a concise summary of the DataFrame
print(df.info())