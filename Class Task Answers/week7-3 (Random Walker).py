import turtle
from random import random  # Import the random function

t = turtle.Turtle()
t.speed(1000)  # Set the drawing speed to a faster value (adjust as needed)

def draw_polygon(side_length, sides):
    for _ in range(0, sides):  # Use a loop to repeat the drawing for the specified number of sides
        if random() < 0.5:
            t.forward(side_length)
            t.right(90)
        else:
            t.forward(side_length)
            t.right(-90)

    turtle.done()

draw_polygon(10, 1000)