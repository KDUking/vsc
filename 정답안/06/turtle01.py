import turtle
import random

turtle.shape("turtle")
r = [10,50,30,70,100,80]
c = ["red","blue","green","orange"]

for i in range(6):
    turtle.pencolor(random.choice(c))
    turtle.pensize(random.randint(1, 10))
    turtle.circle(r[i])
    turtle.forward(70)

turtle.done()