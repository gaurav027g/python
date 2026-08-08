import matplotlib.pyplot as pt

fig = pt.figure()

rect = fig.patch 
rect.set_facecolor('brown')

x = [2,5,9,14]
y = [5,8,12,15]

graph1 = fig.add_subplot(1,1,1,axisbg = 'black')
graph1.plot(x,y,'blue', linewidth = 2)
pt.show()
