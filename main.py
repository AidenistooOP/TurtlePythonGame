import turtle


def draw_shape(shape):
    for i in range(0, 4):
        turtle.fd(50)
        if shape == "square":
            turtle.lt(90)
        elif shape == "triangle":
            turtle.lt(120)
    turtle.fd(75)


turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()

for shape in ["square", "triangle", "square", "triangle"]:
    draw_shape(shape)

turtle.done()
