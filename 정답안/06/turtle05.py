import turtle
turtle.shape("turtle")

dohong = input("도형입력:")
if dohong == "삼각형":
    length = int(input("길이:"))
    size = int(input("라인두께:"))
    turtle.pensize(size)
    turtle.pencolor("red")

    for i in range(3):
        turtle.forward(length)
        turtle.left(120)
elif dohong == "사각형":
    width = int(input("가로:"))
    height = int(input("세로:"))
    size = int(input("라인두께:"))
    turtle.pensize(size)
    turtle.pencolor("blue")

    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
turtle.done()