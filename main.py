import turtle


def draw_shape(shape):
    if shape == "square":
        for i in range(0, 4):
            turtle.fd(50)
            turtle.lt(90)
        turtle.fd(75)

    if shape == "triangle":
        for i in range(3):
            turtle.fd(50)
            turtle.lt(120)
        turtle.fd(75)


turtle.penup()
turtle.goto(-250, 0)
turtle.pendown()

draw_shape("square")
draw_shape("triangle")
draw_shape("square")
draw_shape("triangle")
