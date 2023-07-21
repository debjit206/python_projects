from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        timmy = Turtle("square")
        # timmy.shapesize(stretch_wid=0.5, stretch_len=0.5)
        timmy.color("white")
        timmy.penup()
        timmy.goto(position)
        self.segments.append(timmy)

    def extend_snake(self):
        length = len(self.segments)
        last_segment = self.segments[length - 1]
        self.add_segment(last_segment.position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x_coordinate = self.segments[i - 1].xcor()
            y_coordinate = self.segments[i - 1].ycor()
            self.segments[i].goto(x_coordinate, y_coordinate)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
