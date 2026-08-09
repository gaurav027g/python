import matplotlib.pyplot as pt
import numpy as np

pos = np.arange(6) + 0.5

pt.barh(pos, (4,9,14,5,8,2), align = 'center', color = 'red')

pt.show()
