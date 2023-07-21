from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball
from score import Scoreboard
my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.title("Pong Game")
# my_screen.tracer(n=0)
my_screen.listen()
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
right_score = 0
left_score = 0
ball = Ball()
right_scoreboard = Scoreboard()
left_scoreboard = Scoreboard()
ball.create_ball()
my_screen.onkey(fun=r_paddle.move_up, key="Up")
my_screen.onkey(fun=r_paddle.move_down, key="Down")
my_screen.onkey(fun=l_paddle.move_up, key="w")
my_screen.onkey(fun=l_paddle.move_down, key="s")
game_on = True
x = 0.1
while game_on:
    time.sleep(x)
    my_screen.update()
    ball.move_ball()
    right_scoreboard.score_board(right_score, 100, 280)
    left_scoreboard.score_board(left_score, -100, 280)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.collision_with_wall()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        # print("yes")
        ball.bounce()
        x *= 0.9
        # print(ball.xcor(), ball.ycor())
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce()
        x *= 0.9

    if ball.xcor() > 380:
        ball.reset_position()
        left_score += 1
        left_scoreboard.clear_scoreboard()
        x = 0.1
    if ball.xcor() < -380:
        ball.reset_position()
        right_score += 1
        right_scoreboard.clear_scoreboard()
        x = 0.1
my_screen.exitonclick()
