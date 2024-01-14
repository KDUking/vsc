import turtle
import random

turtle.shape("turtle")
a = ["red","blue","purple","green","orange"]

for i in range(3,6):
    turtle.pencolor(random.choice(a))
    turtle.pensize(random.randint(3,8))
    turtle.up()
    turtle.forward(i)
    turtle.goto(random.randint(-300,300),random.randint(-300,300))
    turtle.down()

turtle.done()

#turtle.circle(random.randint(10,70), steps=random.randint(3,8))
#turtle.pencolor(random.random())
#turtle.pensize(random.randint(10))
#
#