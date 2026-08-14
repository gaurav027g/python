from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as pt
import numpy as np

fig = pt.figure()
chart = fig.add_subplot(1,1,1, projection = '3d')

x,y,z = axes3d.get_test_data(0.05)
chart.plot_wireframe(x,y,z, rstride=10, cstride=2)

chart.set_xlabel('X axis')
chart.set_ylabel('Y axis')
chart.set_zlabel('Z axis')

pt.show()

