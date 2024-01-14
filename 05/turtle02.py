import turtle
turtle.shape("turtle")

distance = int(input("라인길이:"))

a = ["red","blue","purple"]
b = [2,7,9]

for i in range(3):
    turtle.pencolor(a[i])
    turtle.pensize(b[i])
    turtle.forward(distance)
    turtle.right(90)

turtle.done()