import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Alice'],
    'Age': [25, np.nan, 35, 45, 29, 25],
    'Salary': [50000, 60000, -9999, 80000, 70000, 50000], 
    'Department': ['HR', 'Finance', 'finance', 'IT', None, 'HR']
}
df = pd.DataFrame(data)
print("Original Data:\n", df)
imputer = SimpleImputer(strategy='mean')
df['Age'] = imputer.fit_transform(df[['Age']])
df['Department'] = df['Department'].fillna('Unknown')
df['Salary'] = df['Salary'].replace(-9999, np.nan)
df['Salary'] = imputer.fit_transform(df[['Salary']])
df['Department'] = df['Department'].str.capitalize()
df = df.drop_duplicates()
scaler = StandardScaler()
df[['Age', 'Salary']] = scaler.fit_transform(df[['Age', 'Salary']])
print("\nCleaned & Preprocessed Data:\n", df)