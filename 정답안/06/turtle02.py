import turtle
import random

turtle.shape("turtle")
c = ["red","green","blue","purple","orange"]
for i in range(30):
    turtle.up()
    turtle.goto(random.randint(-300,300),random.randint(-300,300))
    turtle.color(random.choice(c))
    turtle.shapesize(random.randint(1,4))
    turtle.right(random.randint(-180,180))
    turtle.stamp()

turtle.done()