import turtle
turtle.shape("turtle")
length = int(input("길이:"))

a = ["red","blue","yellow","green","purple"]
b = [1,3,5,2,8]

for i in range(5):
    turtle.pencolor(a[i])
    turtle.forward(length *b[i])
    turtle.right(45)

turtle.done()

#c = [2,1,6,3,5]
#for i in range(5):
# turtle.pencolor(a[i])
# turtle.pensize(c[i])
# turtle.forward(length *b[i])
# turtle.right(45)
# 
# turtle.done()
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
