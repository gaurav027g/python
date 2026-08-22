import pandas as pd
newCSV = pd.read_csv('TestData.csv', header = 0, names = ["Food", "Price", "Quantity"], usecols = [1,2,3])
print(newCSV)

newCSV.to_csv('TestData2.csv')
newCSV = pd.read_csv('TestData2.csv')
print(newCSV)