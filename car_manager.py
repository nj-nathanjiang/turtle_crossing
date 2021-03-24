import turtle as t
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1


def next_level():
    global STARTING_MOVE_DISTANCE
    STARTING_MOVE_DISTANCE += MOVE_INCREMENT


class CarManager(t.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(180)
        self.y = round(random.randint(-250, 250) / 10) * 10
        self.x = 300
        self.goto(self.x, self.y)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))

    def go_forward(self):
        self.forward(STARTING_MOVE_DISTANCE)
