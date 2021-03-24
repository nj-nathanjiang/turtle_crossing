import time
import random
from turtle import Screen
from player import Player
from car_manager import next_level, CarManager
from scoreboard import Scoreboard

num_players = int(input("Do you want to play 1 player or 2 player? Please enter a number: "))
if num_players == 2:
    print("Hint: You are teammates. Only one of you can move at a time."
          " At the end, move slowly so you don't accidentally crash into a car.")
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

if num_players == 2:
    player_2 = Player()
    player_2.goto(-100, -280)
    player_1 = Player()
    player_1.goto(100, -280)
else:
    player_2 = Player()
    player_2.color("white")
    player_1 = Player()

scoreboard = Scoreboard()
scoreboard.write_level()

screen.listen()
screen.onkey(player_1.go_up, "Up")
screen.onkey(player_2.go_up, "w")

car_spawning_number = 6
players = [player_1, player_2]
cars = []
game_is_on = True
while game_is_on:
    for player in players:
        for car in cars:
            if player.distance(car) < 30:
                game_is_on = False
                scoreboard.game_over()

    number = random.randint(1, 6)
    if number == car_spawning_number:
        car = CarManager()
        cars.append(car)
        car_spawning_counter = 0

    for car in cars:
        car.go_forward()

    time.sleep(0.1)
    screen.update()

    if num_players == 2:
        if player_1.ycor() > 280 and player_2.ycor() > 280:
            player_1.next_level()
            player_2.next_level()
            scoreboard.next_level()
            scoreboard.write_level()
            next_level()

    else:
        if player_1.ycor() > 280:
            player_1.next_level()
            scoreboard.next_level()
            scoreboard.write_level()
            next_level()

screen.exitonclick()

