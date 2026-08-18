import pandas as pd
s = pd.Series([10, "Namaste", 23.5, "Hello"])
print(s)

print(s[0])
print(s[1])

s = pd.Series([10, "Namaste", 23.5, "Hello"], index = ["a", "b", "c", "d"])
print(s)

print(s["b"])

p = {"Bihar": "12.8 crore", "Uttar Pradesh": "24.3 crore", "Maharashtra": "12.9 crore"}
cities = pd.Series(p)
print(cities)

print(cities[cities > "11 crore"])
print(cities[cities > "15 crore"])
print(cities[cities == "12.8 crore"])