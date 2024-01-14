import turtle
turtle.shape("turtle")

turtle.circle(100)

for i in range(3, 7):
    turtle.circle(100, steps=i)
    
turtle.done()