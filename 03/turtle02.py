import turtle
turtle.shape("turtle")

length = int(input("길이:"))
color = input("색깔:")
size = int(input("라인두깨:"))

turtle.pencolor(color)
turtle.pensize(size)

for i in range(3):
    turtle.forward(length)
    turtle.left(120)

turtle.done()