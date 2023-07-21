from turtle import Screen
from race import Race
all_turtle = []
my_screen = Screen()
my_screen.setup(width=500, height=400)
user_guess = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
turtle_race = Race(turtle_list=all_turtle, user_guess=user_guess)
turtle_race.create_turtle()
is_race_on = False
if user_guess:
    is_race_on = True
while is_race_on:
    temp = turtle_race.move_turtle()
    if temp is False:
        is_race_on = False
my_screen.exitonclick()
