import pandas as pd
data = pd.read_csv('TestData.csv')
print(data)

data = pd.read_csv('TestData.csv', names = ["DOB", "Alphabet", "Rank1", "Rank2"])
print(data)

data = pd.read_csv('TestData.csv', names = ["DOB", "Alphabet", "Rank1", "Rank2"], header = 0)
print(data)

data = pd.read_csv('TestData.csv', usecols = [0,3])
print(data)