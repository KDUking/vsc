import turtle
turtle.shape("turtle")

length = int(input("길이:"))
c = ["red","orange","blue","purple","green"]
l = [1,3,5,2,8]
size = [2,1,6,3,5]

for i in range(5):
    turtle.pencolor(c[i])
    turtle.pensize(size[i])
    turtle.forward(length * l[i])
    turtle.right(45)

turtle.done()
