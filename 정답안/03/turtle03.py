import turtle
turtle.shape("turtle")

r = int(input("반지름:"))
c = input("라인색:")
d = int(input("라인두께:"))

turtle.pencolor(c)
turtle.pensize(d)
turtle.circle(r)

for i in range(3, 7):
    turtle.circle(r, steps=i)


turtle.done()