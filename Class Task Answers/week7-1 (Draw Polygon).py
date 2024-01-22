import turtle


t = turtle.Turtle()

def draw_polygon(side_length, sides):
    for _ in range(0, sides):
        t.forward(side_length)
        t.right(360 / sides)

    turtle.done()

draw_polygon(1, 400)