import turtle
from color_data import color
from random import choice
timmy = turtle.Turtle()
""" .colormode() is a important module while working with rgb"""
turtle.colormode(255)
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
timmy.goto(-200, -200)
# timmy.pendown()
# timmy.setheading(10)


def drawing_dot(var):
    for _ in range(10):
        if _ != 9:
            dot_color = choice(color)
            timmy.dot(20, dot_color)
            # timmy.penup()
            timmy.forward(50)
            # timmy.pendown()
        else:
            dot_color = choice(color)
            timmy.dot(20, dot_color)
    if var % 2 == 0:
        timmy.left(90)
        # timmy.penup()
        timmy.forward(50)
        # timmy.pendown()
        timmy.left(90)
    else:
        timmy.right(90)
        # timmy.penup()
        timmy.forward(50)
        # timmy.pendown()
        timmy.right(90)


for i in range(10):
    drawing_dot(i)

my_screen = turtle.Screen()
my_screen.exitonclick()
