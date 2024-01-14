import turtle
turtle.shape("turtle")

length = int(input("길이:"))
size = [2, 7, 9]
c = ["red", "blue", "purple"]

for i in range(3):
    turtle.pencolor(c[i])
    turtle.pensize(size[i])
    turtle.forward(length)
    turtle.right(90)

turtle.done()