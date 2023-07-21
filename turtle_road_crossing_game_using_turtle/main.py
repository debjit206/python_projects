import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.onkey(fun=player.move, key="Up")
game_is_on = True
score = 1
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    scoreboard.score(score)
    for car in car_manager.car_list:
        if player.distance(car) < 30:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() > 270:
        player.reset_position()
        score += 1
        car_manager.car_speed += 5
        scoreboard.clear_scoreboard()

screen.exitonclick()
