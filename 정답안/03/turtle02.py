import turtle
turtle.shape("turtle")

length = int(input("길이:"))
size = int(input("라인두께:"))
color = input("라인색:")

turtle.pensize(size)
turtle.pencolor(color)

# turtle.forward(length)
# turtle.left(120)

# turtle.forward(length)
# turtle.left(120)

# turtle.forward(length)
# turtle.left(120)

for i in range(3):
    turtle.forward(length)
    turtle.left(120)

turtle.done()