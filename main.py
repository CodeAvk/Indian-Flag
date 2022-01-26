import turtle

t = turtle.Turtle()
t.pensize(5)
t.speed(10)
def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

#Ashok Chakra
t.color("#054188")
for i in range(24):
    t.forward(80)
    t.backward(80)
    t.left(15)
move(0, -80)
t.circle( 80, 360)

#Green
t.begin_fill()
t.color("green")
t.forward(350)
t.backward(700)
t.right(90)
t.forward(200)
t.left(90)
t.forward(700)
t.left(90)
t.forward(200)
t.left(90)
t.end_fill()

#Orange
t.color("orange")
move(-350, 80)
t.begin_fill()
t.right(180)
t.forward(700)
t.left(90)
t.forward(200)
t.left(90)
t.forward(700)
t.left(90)
t.forward(200)
t.end_fill()


