import turtle
turtle.shape("turtle")

length = int(input("길이:"))
color = input("색깔:")
size = int(input("두께:"))

turtle.pencolor(color)
turtle.pensize(size)

turtle.circle(length)

for i in range(3, 7):
   turtle.circle(length, steps=i)
    
turtle.done()
