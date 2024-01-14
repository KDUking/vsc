import turtle
turtle.shape("turtle")

def circle_draw(r):
    s = r * r * 3.14
    turtle.circle(r)
    turtle.write(s)
    return s

b = int(input("반지름:"))

r = circle_draw(b)

print("원 면적: %.2f" % r)

turtle.done()