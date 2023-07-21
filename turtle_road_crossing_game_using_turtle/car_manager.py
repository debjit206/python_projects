from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
# MOVE_INCREMENT = 10
X_POSITION = 300


class CarManager:
    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_number = random.randint(1, 6)
        if random_number == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            y_cor = random.randint(-250, 250)
            car.goto(X_POSITION, y_cor)
            self.car_list.append(car)

    def move_car(self):
        for car in self.car_list:
            car.backward(self.car_speed)
