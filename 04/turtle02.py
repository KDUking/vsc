import turtle
turtle.shape("turtle")

length = int(input("길이:"))
dis = int(input("간격:"))

for i in range(3):
    turtle.goto(0,-dis*i)
    turtle.down()
    turtle.forward(length + dis*i)
    turtle.up()

turtle.done()