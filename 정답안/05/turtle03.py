import turtle
turtle.shape("turtle")

length = int(input("길이:"))
a = [100, 40, 30, 70, 10, 90]
c = ["red","blue","yellow","orange","pink","purple"]
dis = 0 # 간격

for i in range(6):
    dis += a[i]
    turtle.up()
    turtle.goto(0, dis)
    turtle.down()
    turtle.pencolor(c[i])
    turtle.forward(length)

turtle.done()