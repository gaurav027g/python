import pandas as pd
headers = ['name', 'title', 'department', 'salary']
chicago = pd.read_csv('chicago data.csv', header=None, names=headers)
print(chicago.head())

dept = chicago.groupby('department')
print(dept.count().head())

print(dept.size().head())