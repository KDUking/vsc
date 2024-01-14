import turtle

turtle.shape("turtle")
c = ["red","blue","purple"]

# turtle.pencolor("red")
# turtle.forward(100)
# turtle.left(120)

# turtle.pencolor("blue")
# turtle.forward(100)
# turtle.left(120)

# turtle.pencolor("purple")
# turtle.forward(100)
# turtle.left(120)

for i in range(3):
    turtle.pencolor(c[i])
    turtle.forward(100)
    turtle.left(120)

turtle.done()