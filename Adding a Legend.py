import matplotlib.pyplot as pt

sizes = [50,20,20,7,3]

labels = ['Android', 'Apple', 'Microsoft', 'Blackberry', 'Xiaomi']
colors = ["yellow", "orange", "blue", "red", "grey"]

pt.pie(sizes, colors = colors, startangle=90, labels = labels)
pt.title('Pie Chart')
pt.legend(title = 'Legend', loc = 'lower left')

pt.axis('equal')
pt.show()
