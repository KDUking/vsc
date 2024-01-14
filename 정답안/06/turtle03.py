import turtle
import random

turtle.shape("turtle")
c = ["red","green","blue","purple","orange","black"]
for i in range(30):
    turtle.goto(0, 0)
    turtle.right(random.randint(-180,180))
    turtle.pencolor(random.choice(c))
    turtle.pensize(random.randint(1,10))
    turtle.forward(random.randint(1, 300))

turtle.done()