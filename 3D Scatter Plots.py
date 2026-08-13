from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as pt
import numpy as np

fig = pt.figure()

chart = fig.add_subplot(1,1,1, projection = '3d')

X,Y,Z = np.array([1,2,3,4,5,6,7,8]), np.array([2,5,3,8,9,5,6,1]), np.array([3,6,2,7,5,4,5,6])

X,Y = np.meshgrid(X,Y)

Z = np.tile(Z, (8,1))

chart.scatter(X,Y,Z, c = 'red', marker = 'o')

chart.set_xlabel('x axis')
chart.set_ylabel('y axis')
chart.set_zlabel('z axis')

pt.show()
