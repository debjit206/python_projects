from turtle import Turtle, Screen
ALIGNMENT = "center"
FONT = ('Arial', 15, 'normal')
my_screen = Screen()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        # self.my_screen = Screen()
        # self.write("Home = ", True, align="center")

    def score_board(self, score, x, y):
        my_screen.tracer(n=0)
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.goto(x, y)
        score_str = f"score: {score}"
        self.write(score_str, False, align=ALIGNMENT, font=FONT)
        my_screen.update()

    def clear_scoreboard(self):
        # self.my_screen.tracer(n=0)
        self.clear()
        # self.my_screen.update()

    def game_over(self):
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)
