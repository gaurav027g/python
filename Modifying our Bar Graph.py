import matplotlib.pyplot as pt
import numpy as np

pos = np.arange(6) + 0.5

names = ['Avi', 'Jose', 'Bob', 'Nick', 'Zelda', 'Matt']

pt.barh(pos, (4,9,14,5,8,2), align = 'center', color = 'red')

pt.title('Height of Students in Inches', color = 'blue')
pt.xlabel('Height in Inches', color = 'black')
pt.ylabel('Students', color = 'black')

pt.tick_params(axis = 'x', color = 'black')
pt.tick_params(axis = 'y', color = 'black')

pt.yticks(pos, names)

pt.subplots_adjust(left = 0.11, bottom = 0.12, right = 0.94)

pt.gcf().set_facecolor('lightblue')
pt.gca().set_facecolor('gray')

pt.show()
