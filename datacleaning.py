import numpy as np
import pandas as pd
data = {
    'ID': [1, 2, 3, 4, 5, 6],
    'Name': [' Alice ', 'Bob', 'Charlie', 'DAVID', 'eve', 'Bob'],
    'Age': ['25', '30', None, '45', '29', '30'],
    'Salary': ['50,000', '60,000', '70,000', '80,000', None, '60,000'],
    'JoiningDate': ['2020-01-01', '2021/02/15', '15-03-2022', None, '2020-01-01', '2021/02/15']
}
df = pd.DataFrame(data)
print("Original Data:\n", df)
df['Name'] = df['Name'].str.strip().str.capitalize()
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df['Salary'] = df['Salary'].str.replace(',', '', regex=True)
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
df['Age'].fillna(method='ffill', inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
df['JoiningDate'].fillna('2020-01-01', inplace=True)
df['JoiningDate'] = pd.to_datetime(df['JoiningDate'], errors='coerce', dayfirst=True)
df = df.drop_duplicates()
print("\nCleaned Data:\n", df)