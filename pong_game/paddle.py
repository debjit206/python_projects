from turtle import Turtle
MOVEMENT = 20


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.penup()
        x_coordinate = self.x_cor
        y_coordinate = self.y_cor
        self.goto(x_coordinate, y_coordinate)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.color("white")

    def move_up(self):
        self.forward(MOVEMENT)

    def move_down(self):
        self.backward(MOVEMENT)
