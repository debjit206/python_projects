from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.move_x = 10
        self.move_y = 10

    def create_ball(self):
        self.shape("circle")
        self.penup()
        self.color("white")

    def move_ball(self):
        x_coordinate = self.xcor() + self.move_x
        y_coordinate = self.ycor() + self.move_y
        # print(x_coordinate,y_coordinate)
        self.goto(x_coordinate, y_coordinate)

    def collision_with_wall(self):
        self.move_y *= -1

    def bounce(self):
        self.move_x *= -1

    def reset_position(self):
        self.goto(0,0)
        self.bounce()

