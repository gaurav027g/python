import matplotlib.pyplot as pt

sizes = [50,20,20,7,3]

colors = ["yellow", "orange", "blue", "red", "grey"]

pt.pie(sizes, colors = colors, startangle=90)

pt.axis('equal')
pt.show()
