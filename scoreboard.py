from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-240, 274)
        self.level_number = 1

    def write_level(self):
        self.clear()
        self.write(f"Level: {self.level_number}", align="center", font=FONT)

    def next_level(self):
        self.level_number += 1

    def game_over(self):
        self.goto(0, -26)
        self.write("GAME OVER", align="center", font=FONT)
