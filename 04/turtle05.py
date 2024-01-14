import turtle
import random

turtle.shape("turtle")
for i in range(50):
    turtle.up()
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    turtle.goto(x,y)
    turtle.down()
    turtle.circle(random.randint(10,60))
turtle.done()