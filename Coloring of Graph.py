import matplotlib.pyplot as pt

fig = pt.figure()

rect = fig.patch 
rect.set_facecolor('brown')

x = [2,4,9,14]
y = [5,8,12,15]

graph1 = fig.add_subplot(1,1,1)
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

pt.show()
