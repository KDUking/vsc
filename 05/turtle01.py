import turtle
turtle.shape("turtle")

a = ["red","blue","purple"]


for i in range(3):
    turtle.pencolor(a[i])
    turtle.forward(100)
    turtle.left(120)
    
turtle.done()