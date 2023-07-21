from turtle import Turtle, Screen
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
my_screen = Screen()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

    def score(self, score):
        my_screen.tracer(n=0)
        self.penup()
        self.hideturtle()
        self.color("black")
        self.speed("fastest")
        self.goto(-230, 270)
        score_str = f"LEVEL: {score}"
        self.write(score_str, False, align=ALIGNMENT, font=FONT)
        my_screen.update()

    def clear_scoreboard(self):
        # self.my_screen.tracer(n=0)
        self.clear()
        # self.my_screen.update()

    def game_over(self):
        self.penup()
        self.hideturtle()
        self.color("black")
        self.speed("fastest")
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)
