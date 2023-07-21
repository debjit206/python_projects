from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(n=0)
my_screen.listen()
snake = Snake()
food = Food()
scoreboard = Scoreboard()
my_screen.onkey(fun=snake.up, key="Up")
my_screen.onkey(fun=snake.down, key="Down")
my_screen.onkey(fun=snake.left, key="Left")
my_screen.onkey(fun=snake.right, key="Right")

game_on = True
score = 0
while game_on:
    my_screen.update()
    time.sleep(0.13)
    snake.move()
    scoreboard.score()
    scoreboard.high_score()
    if snake.head.distance(food) < 15:
        food.create_new_food()
        scoreboard.clear_scoreboard()
        snake.extend_snake()
        scoreboard.update_score()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        scoreboard.update_high_score()
        scoreboard.game_over()

    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            game_on = False
            scoreboard.update_high_score()
            scoreboard.game_over()


my_screen.exitonclick()
