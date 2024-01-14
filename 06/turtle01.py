import turtle
import random

turtle.shape("turtle")

length = int(input("길이:"))
radius = int(input("반지름:"))
color = ["red","blue","green","purple"]
b = [10,50,30,70,100,80]

for i in range(6):
    turtle.pencolor(color[i])
    turtle.up()
    turtle.forward(random.randint(length*[i],b))
    turtle.forward(radius,b)
    turtle.down()

turtle.done()

#import turtle
#import random
# 
#turtle.shape("turtle")
#b = [10,50,30,70,100,80]
#color = ["red","blue","green","purple"]
# 
#for i in range(6):
#    turtle.pencolor(random.choice(color))
#    turtle.pensize(random.randint(1,10))
#    turtle.circle(b[i])
#    turtle.forward(70)
#
#turtle.done()