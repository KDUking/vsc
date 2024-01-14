import turtle
import random

turtle.shape("turtle")

a = ["red","purple","blue","brown","yellow"]

for i in range(30):
    turtle.goto(0,0)
    turtle.right(random.randint(-180,180))
    turtle.pensize(random.randint(1,10))
    turtle.color(random.choice(a))
    turtle.forward(random.randint(1,500))

turtle.done()