import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossy")
screen.listen()

cars = []
for _ in range(10):
    new_car = CarManager()
    cars.append(new_car)
player = Player()
scoreboard = Scoreboard()


screen.onkeypress(player.move_forward, "Up")
screen.onkeypress(player.move_backward, "Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for car in cars:
        car.move()

    # Detect if player reached top of screen
    if player.ycor() >= 280:
        scoreboard.increase_level()
        player.reset_position()
        for car in cars:
            car.increase_speed()
    # Detect if player collided with car
    if abs(player.ycor() - car.ycor()) <= 20 and player.distance(car) < 20:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
