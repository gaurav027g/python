import pandas as pd
users = pd.read_csv('u.user', sep = "|", names = ["User_ID", "Age", "Gender", "Occupation", "Zip_Code"])

print(users.head())

print(users.dtypes)

print(users.describe)

print(users.set_index('User_ID').head())

print(users.head())

users.set_index('User_ID', inplace = True)
print(users)

print(users[10:15])

print(users.loc[[2,4,67]])