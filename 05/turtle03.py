import turtle
turtle.shape("turtle")

length = int(input("길이:"))
dis = 0

a = [100,40,30,70,10,90]
b = ["red","blue","yellow","orange","pink","purple"]

for i in range(6):
    dis += a[i]
    turtle.up()
    turtle.pencolor(b[i])
    turtle.goto(0,dis)
    turtle.down()
    turtle.forward(length)
    
turtle.done()