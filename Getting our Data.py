import pandas as pd
users = pd.read_csv('movies.csv', sep = "|", names = ["User_ID", "Age", "Gender", "Occupation", "Zip_Code"])
print(users.head())
