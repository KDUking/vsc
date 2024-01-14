import turtle
turtle.shape("turtle")

def c_area(r, x, y):
    area = r * r * 3.14
    round = 2 * r * 3.14
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.circle(r)
    turtle.write(round, area)
    return area, round

radius = int(input("반지름:"))
px = int(input("x좌표:"))
py = int(input("y좌표:"))

#함수 호출
a, r = c_area(radius, px, py)
print("반지름:%d 면적:%.2f 둘레:%.2f" % (radius, a, r))

turtle.done()