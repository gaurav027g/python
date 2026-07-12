import turtle
t = turtle.Pen()
def square(side):
    for p in range(0,5):
        t.forward(side)
        t.left(90)
square(100)
t.up()
t.left(45)
t.forward(200)
t.down()
def circle(radius):
    t.circle(radius)
circle(100)
