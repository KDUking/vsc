import turtle
turtle.shape("turtle")

def rect(width, height):
    result = width * height
    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.write(result)
    return result

w = int(input("가로:"))
h = int(input("세로:"))

#함수 호출
r = rect(w, h)
print("가로:{} 세로:{} 넓이:{}".format(w,h,r))

turtle.done()