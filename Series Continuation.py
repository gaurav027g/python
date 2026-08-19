import pandas as pd
s = pd.Series([10, "Namaste", 23.5, "Hello"])
print(s)

print(s[0])
print(s[1])

s = pd.Series([10, "Namaste", 23.5, "Hello"], index = ["a", "b", "c", "d"])
print(s)

print(s["b"])

p = {"Bihar": 12.8, "Uttar Pradesh": 24.3, "Maharashtra": 12.9, "West bangal": 9.1, "Rajasthan": 6.8}
cities = pd.Series(p)
print(cities)

print(cities > 6)

cities["Bihar"] = 12.9
print(cities)

cities[cities > 12] = 10
print(cities)

print('Bihar' in cities)
print('Punjab' in cities)

import numpy as np
print(np.square(cities))

print(cities.isnull())

print(cities/10)