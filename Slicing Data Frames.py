import pandas as pd
users = pd.read_csv('u.user', sep = "|", names = ["User_ID", "Age", "Gender", "Occupation", "Zip_Code"])
print(users.head())

print(users.tail())
print(users.tail(2))
print(users.head(3))
print(users[10:15])
print(users[:10])
print(users[195:])
print(users[:-1])