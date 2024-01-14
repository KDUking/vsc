import turtle
import random

turtle.shape("turtle")
a = ["red","blue","purple","green","orange"]

for i in range(30):
    turtle.pencolor(random.choice(a))
    turtle.pensize(random.randint(1, 10))
    turtle.up()
    turtle.goto(random.randint(-300,300), random.randint(-300,300))
    turtle.down()
    #turtle.circle(random.randint(10,70))
    turtle.circle(random.randint(10,70), steps= random.randint(3, 8))

turtle.done()