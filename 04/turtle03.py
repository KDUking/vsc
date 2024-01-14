import turtle
turtle.shape("turtle")

r = int(input("반지름:"))

turtle.circle(r)
turtle.right(360)
turtle.circle(r/2)

turtle.done()

#turtle.up()
#turtle.goto(0,r*2)
#turtle.down()
