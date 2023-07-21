from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.create_new_food()

    def create_new_food(self):
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        x_coordinate = random.randint(-270, 270)
        y_coordinate = random.randint(-270, 270)
        self.goto(x_coordinate, y_coordinate)
