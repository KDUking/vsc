import turtle
turtle.shape("turtle")

def circle_draw(r):
    area = r * r * 3.14
    round = 2 * r * 3.14
    turtle.up()
    turtle.goto(50,50)
    turtle.down()
    turtle.circle(r)
    turtle.write(area,round)
    return area,round

b = int(input("반지름:"))

r = circle_draw(b)

print("원넓이:{}".format(r))

turtle.done()