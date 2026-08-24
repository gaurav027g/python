import pandas as pd
frame1 = pd.DataFrame({'key': range(5), 'frame1': ["a", "b", "c", "d", "e"]})
frame2 = pd.DataFrame({'key': range(2,7), 'frame2': ["u", "v", "w", "x", "y"]})

print(frame1)
print(frame2)

print(pd.merge(frame1, frame2))

print(pd.merge(frame1, frame2, how = 'right'))

print(pd.merge(frame1, frame2, how = 'left'))

print(pd.merge(frame1, frame2, how = 'inner'))

print(pd.merge(frame1, frame2, how = 'outer'))

print(pd.concat([frame1, frame2]))

print(pd.concat([frame1, frame2], axis = 1))