import pandas as pd
users = pd.read_csv('ml-100k/u.user', sep = "|", names = ["User_ID", "Age", "Gender", "Occupation", "Zip_Code"])
print(users.head())
