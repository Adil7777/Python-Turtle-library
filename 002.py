import turtle

turtle.bgcolor('black')
turtle.pensize(2)
turtle.speed(0)
colors = ['red', 'magenta', 'blue', 'cyan', 'green', 'yellow', 'white']

for i in range(6):
    for color in colors:
        turtle.color(color)
        turtle.circle(100)
        turtle.left(10)
turtle.hideturtle()

