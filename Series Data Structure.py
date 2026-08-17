import pandas as pd
s = pd.Series([10, "Namaste", 23.5, "Hello"])
print(s)

print(s[0])
print(s[1])

s = pd.Series([10, "Namaste", 23.5, "Hello"]), index = ["a", "b", "c", "d"]
print(s)