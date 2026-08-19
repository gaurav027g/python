import pandas as pd
s = pd.Series([10, "Namaste", 23.5, "Hello"])
print(s)

print(s[0])
print(s[1])

s = pd.Series([10, "Namaste", 23.5, "Hello"], index = ["a", "b", "c", "d"])
print(s)

print(s["b"])

p = {"Bihar": "12.8 crore", "Uttar Pradesh": "24.3 crore", "Maharashtra": "12.9 crore", "West bangal": "9.1 crore", "Rajasthan":
     "6.8 crore"}
cities = pd.Series(p)
print(cities)

print(cities > "6 crore")
cities["Bihar"] = "12.9 crore"
print(cities)
#some problem

cities[cities > "12 crore"] = "10 crore"
print(cities)
#some problem

print('Bihar' in cities)
print('Punjab' in cities)

import numpy as np
np.square(cities)
#some problem