import turtle
turtle.shape("turtle")

a = int(input("방향1:가로, 2:세로:"))
length = int(input("길이:"))

if a == 1:
    turtle.pencolor("red")
    turtle.forward(length)
elif a == 2:
    turtle.right(90)
    turtle.pencolor("blue")
    turtle.forward(length)

turtle.done()