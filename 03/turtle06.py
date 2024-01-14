import turtle
turtle.shape("turtle")

length = int(input("길이:"))

for i in  range(5):
    turtle.forward(length /(2**i))
    turtle.right(45)

turtle.done()