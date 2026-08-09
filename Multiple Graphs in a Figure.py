import matplotlib.pyplot as pt

fig = pt.figure()

rect = fig.patch 
rect.set_facecolor('brown')

x = [0,7,8,12]
y = [5,13,2,8]
x2 =[0,4,7,12]
y2 =[3,7,1,12]
x3 =[0,4,6,8]
y3 =[13,5,8,2]

graph1 = fig.add_subplot(2,1,1)
graph1.set_facecolor('black')
graph1.plot(x,y,'blue', linewidth = 2)


graph1.tick_params(axis="x", color = "white")
graph1.tick_params(axis="y", color = "white")

graph1.spines["top"].set_color('white')
graph1.spines["bottom"].set_color('white')
graph1.spines["left"].set_color('white')
graph1.spines["right"].set_color('white')

graph1.set_title('Random Graph', color='white')
graph1.set_xlabel('This is the x axis', color='white')
graph1.set_ylabel('This is the y axis', color='white')

graph2 = fig.add_subplot(2,1,2)
graph2.set_facecolor('black')
graph2.plot(x3,y3,'red', linewidth = 2)


graph2.tick_params(axis="x", color = "white")
graph2.tick_params(axis="y", color = "white")

graph2.spines["top"].set_color('white')
graph2.spines["bottom"].set_color('white')
graph2.spines["left"].set_color('white')
graph2.spines["right"].set_color('white')

graph2.set_title('Random Graph', color='white')
graph2.set_xlabel('This is the x axis', color='white')
graph2.set_ylabel('This is the y axis', color='white')

pt.show()
