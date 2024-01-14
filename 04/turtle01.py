import turtle
turtle.shape("turtle")

length = float(input("길이:"))
distance = float(input("간격:"))

for i in range(3):
    turtle.forward("length")
    turtle.goto(0, 50)

turtle.done()


#length = int(input(길이:))
#dis = int(input("간격:"))
#
#turtle.goto(0,-dis*0)
#turtle.down()
#turtle.forward(length)
#turtle.up()
#
#for i in range(3):
#  turtle.goto(0,-dis*i)
#  turtle.down()
#  turtle.forward(length)
#  turtle.up()
#
#turtle.done()