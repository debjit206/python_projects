from turtle import Turtle, Screen
ALIGNMENT = "center"
FONT = ('Arial', 15, 'normal')
my_screen = Screen()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.game_score = 0
        with open("data.txt") as file:
            self.game_high_score = int(file.read())
        # self.my_screen = Screen()
        # self.write("Home = ", True, align="center")

    def score(self):
        my_screen.tracer(n=0)
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.goto(-100, 280)
        score_str = f"Score: {self.game_score}"
        self.write(score_str, False, align=ALIGNMENT, font=FONT)
        my_screen.update()

    def clear_scoreboard(self):
        # self.my_screen.tracer(n=0)
        self.clear()
        # self.my_screen.update()

    def update_score(self):
        self.game_score += 1

    def game_over(self):
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)

    def high_score(self):
        my_screen.tracer(n=0)
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.goto(100, 280)
        score_str = f"High Score: {self.game_high_score}"
        self.write(score_str, False, align=ALIGNMENT, font=FONT)
        my_screen.update()

    def update_high_score(self):
        if self.game_score > self.game_high_score:
            new_high_score = f"{self.game_score}"
            with open("data.txt", "w") as file:
                file.write(new_high_score)
