import turtle
t = turtle.Pen()

for p in range(0,8):
    t.forward(100)
    t.left(225)

t.left(45)
t.forward(100)
for p in range(0,8):
    t.forward(100)
    t.left(225)

t.reset()
for p in range(0,8):
    t.forward(100)
    t.left(225)
t.up()
t.left(45)
t.forward(100)
t.down()
for p in range(0,8):
    t.forward(100)
    t.left(225)

