import turtle
turtle.shape("turtle")

def c_area(r):
    result = r * r * 3.14
    turtle.circle(r)
    turtle.write(result)
    return result

radius = int(input("반지름:"))

r = c_area(radius)
print("원 면적: %.2f" % r)

turtle.done()