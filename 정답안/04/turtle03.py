import turtle

radius = int(input("반지름:"))
turtle.shape("turtle")

turtle.circle(radius)
turtle.up()
turtle.goto(0, radius*2)
turtle.down()
turtle.circle(radius/2)

turtle.done()