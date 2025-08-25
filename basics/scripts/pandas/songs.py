import pandas as pd

# Load csv file
df = pd.read_csv('resources/songs.csv')

print(df[['Duration']])

print(df[['Artist', 'Title', 'Release_Date']])

# Accessing individual cells
print(df.at[0, 'Title'])  # First song title
print(df.iat[0, 1])       # First song artist

# Using iloc
print(df.iloc[0, 1])       # First song artist
print(df.iloc[0, 2])       # First song release date

# Using ranges in iloc (slicing)
print(df.iloc[0:2, 0:2])   # First two rows with first 2 columns
print(df.loc[0:3, 'Title':'Release_Date'])

new_df = df.loc[0:3, 'Title':'Release_Date']
# transform dataframe Release_Date to Release_year
# Add new column with the data transformed
new_df['Release_Year'] = pd.to_datetime(new_df['Release_Date']).dt.year
# Drop Release_Date
new_df = new_df.drop(columns=['Release_Date'])
print("With release year\n:", new_df)

df2 = df[['Title', 'Artist', 'Release_Date']].copy()
df2['Release_Year'] = pd.to_datetime(df2['Release_Date']).dt.year
df2 = df2.drop(columns=['Release_Date'])
df_after_1979 = df2[df2['Release_Year']>1979]
print("Release year > 1979:\n", df_after_1979)
# save
df_after_1979.to_csv('tmp/songs_after_1979.csv', index=False)

# Working with Series
data = [10, 20, 30]
s = pd.Series(data)
print("Series:\n", s)
# change index to labels (dynamically)
s.index = s.index.map(lambda x: f'CustomLabel_{x}')
print("Series with labels:\n", s)

# access by label
print("Accessing by label:\n", s['CustomLabel_0'])
# access by position
print("Accessing by position:\n", s.iloc[0])
# access multiple elements
print("Accessing multiple elements:\n", s[0:2])

# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
person_df = pd.DataFrame(data)
print("DataFrame from dictionary:\n", person_df)

# column selection
print("Column selection 1:\n", person_df['Name']) # returns a Series
print("Column selection 2:\n", person_df[['Name']]) # returns a DataFrame
print("Column selection:\n", person_df[['Name', 'Age']])

# row selection
# by position
print("Row selection:\n", person_df.iloc[0])
# by label
print("Row selection:\n", person_df.loc[0]) # in this case 0 is a label also

# slicing rows
print("Row selection:\n", person_df.loc[0:2]) # in this case 0:2 is a label also
# slicing columns
print("Column selection:\n", person_df.loc[:, 'Name':'Age'])

# unique
print("Unique values in 'City' column:\n", person_df['City'].unique())

# filtering
print("Filtering rows where Age > 30:\n", person_df[person_df['Age'] > 30])
