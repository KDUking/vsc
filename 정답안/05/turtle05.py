import turtle
import random
turtle.shape("turtle")

length = int(input("길이:"))
c = ["red","orange","blue","purple","green"]
l = [1,3,5,2,8]

for i in range(5):
    turtle.pencolor(random.choice(c))
    turtle.pensize(random.randint(1, 10))
    turtle.forward(length / l[i])
    turtle.right(45)

turtle.done()