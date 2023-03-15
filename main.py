import turtle


def draw_shape(shape):
    for i in range(0, 4):
        turtle.fd(50) if shape == "square" else turtle.fd(50), turtle.lt(
            120) if shape == "triangle" else turtle.lt(90)
    turtle.fd(75)


turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

for shape in ["square", "triangle", "square", "triangle"]:
    draw_shape(shape)
