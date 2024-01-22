import turtle

def draw_spirograph(circles):
    turtle.speed(circles[0]['speed'])
    turtle.bgcolor("black")
    turtle.pensize(2)

    for circle in circles:
        turtle.color(circle['color'])
        for _ in range(circle['spiral_count']):
            turtle.circle(circle['radius'])
            turtle.left(circle['left_angle'] if circle['left'] else -circle['right_angle'])

    turtle.hideturtle()
    turtle.done()

# Set the parameters for each circle
circles = [
    {'radius': 50, 'color': "cyan", 'spiral_count': 36, 'speed': 0, 'left_angle': 10, 'right_angle': 10, 'left': True},
    {'radius': 100, 'color': "magenta", 'spiral_count': 36, 'speed': 0, 'left_angle': 10, 'right_angle': 10, 'left': False},
    {'radius': 80, 'color': "red", 'spiral_count': 36, 'speed': 0, 'left_angle': 10, 'right_angle': 10, 'left': False},
]

# Draw the spirograph
draw_spirograph(circles)