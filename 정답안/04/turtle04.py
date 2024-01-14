import turtle
import random

turtle.shape("turtle")
for i in range(30):
    turtle.up()
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    turtle.goto(x, y)
    turtle.stamp()

turtle.done()
