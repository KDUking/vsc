import turtle
import random
turtle.shape("turtle")

length = int(input("길이:"))

a = ["red","yellow","blue","green","purple"]
b = [1,3,5,2,8]


for i in range(5):
    turtle.pencolor(a[i])
    turtle.forward(length * b[i])
    turtle.left(45)
turtle.done()

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