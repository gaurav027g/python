import matplotlib.pyplot as pt

x = []
y = []

readFile = open("coordinates.txt", "r")
data = readFile.read().split('\n')

for p in data:
    val = p.split(",")
    x.append(int(val[0]))
    y.append(int(val[1]))

print(data)

print(x)
print(y)

pt.plot(x,y)
pt.show()
