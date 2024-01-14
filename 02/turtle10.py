import turtle
turtle.shape("turtle")

# turtle.goto(0,-50*0)
# turtle.down()
# turtle.forward(100)
# turtle.up()

# turtle.goto(0,-50*1)
# turtle.down()
# turtle.forward(100)
# turtle.up()

# turtle.goto(0,-50*2)
# turtle.down()
# turtle.forward(100)
# turtle.up()

for i in range(3):
    turtle.goto(0,-50 * i)
    turtle.down()
    turtle.forward(100)
    turtle.up()
    
turtle.done()