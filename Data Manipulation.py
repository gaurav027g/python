import pandas as pd
users = pd.read_csv('u.user', sep = "|", names = ["User_ID", "Age", "Gender", "Occupation", "Zip_Code"])

print(users["Gender"].head(10))

columns_I_want = ["Occupation","Zip_Code"]
print(users[columns_I_want].head())

print(users[users.Age > 30].head())

print(users.Zip_Code)

print(users[(users.Age < 25) & (users.Gender == "M")].head(2))

print(users[(users.Occupation == "writer") & (users.Gender == "F")].head())

print(users[(users.Gender == "M") & (users.Age > 50)])

print(users[(users.Gender == "M") & (users.Age > 50)].head())