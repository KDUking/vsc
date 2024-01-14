import turtle
import random

turtle.shape("turtle")

a = ["red","blue","orange","yellow"]

for i in range(30):
    turtle.shapesize(random.randint(1,10))
    turtle.fillcolor(random.choice(a))
    turtle.up()
    turtle.stamp()
    turtle.down()

turtle.done()

#import turtle
#import random
#turtle.shape("turtle")
#a = ["red","blue","orange","yellow"]
# for i in range(30):
#    turtle.up()
#    turtle.goto(random.randint(-300,300),random.randint(-300,300))
#    turtle.color(random.choice(a))
#    turtle.shapesize(random.randint(1,10))
#    turtle.right(random.randint(-180,180))
#    turtle.stamp()
#turtle.done()
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
