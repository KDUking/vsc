import turtle
turtle.shape("turtle")

def rectangle_draw(a,b):
    for i in range(2):
        turtle.forward(m)
        turtle.right(90)
        turtle.forward(n)
        turtle.right(90)
    return rectangle_draw


m = int(input("가로:"))
n = int(input("세로:"))

r = rectangle_draw(m,n)

turtle.done()