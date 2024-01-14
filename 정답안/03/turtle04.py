import turtle
turtle.shape("turtle")

d = int(input("길이:"))
ps = int(input("라인두께:"))
pc = input("라인색:")
tc = input("거북이 색:")

turtle.fillcolor(tc)
turtle.pencolor(pc)
turtle.pensize(ps)

for i in range(3):
    turtle.forward(d)
    turtle.right(90)

turtle.done()

