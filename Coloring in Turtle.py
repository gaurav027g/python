import turtle
t = turtle.Pen()
t.color(0,0,1)
t.begin_fill()
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
t.end_fill()

t.reset()
