import turtle as t

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(t.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.color("black")

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.color("white")
        self.goto(STARTING_POSITION)
        self.color("black")

    def next_level(self):
        self.sety(-280)
