from turtle import Turtle
import random


class Race:
    def __init__(self, turtle_list, user_guess):
        self.turtle_list = turtle_list
        self.user_guess = user_guess

    def create_turtle(self):
        color = ["red", "orange", "yellow", "green", "blue", "purple", "violet"]
        y = 150
        for i in range(0, 7):
            timmy = Turtle(shape="turtle")
            timmy.color(color[i])
            timmy.penup()
            timmy.goto(-240, y)
            self.turtle_list.append(timmy)
            y -= 50

    def is_race_over(self, turtle):
        if turtle.xcor() >= 230:
            turtle_color = turtle.pencolor()
            if turtle_color == self.user_guess:
                result = f"You won. The {turtle_color} turtle is the winner"
                print(result)
                return True
                # my_screen.textinput(title="Result", prompt=result)
            else:
                result = f"You lose, the {turtle_color} turtle is the winner"
                # my_screen.textinput(title="Result", prompt=result)
                print(result)
                return True
        else:
            return False

    def move_turtle(self):
        for turtle in self.turtle_list:
            movement = random.randint(2, 10)
            # turtle.speed("fastest")
            turtle.forward(movement)
            temp = self.is_race_over(turtle)
            if temp is True:
                return False
                # break
