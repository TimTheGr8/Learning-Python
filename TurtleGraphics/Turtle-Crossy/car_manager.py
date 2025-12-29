from turtle import Turtle

import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.create_car()

    def create_car(self):
        self.color(random.choice(COLORS))
        self.penup()
        self.shape("square")
        self.shapesize(1, 2)
        self.starting_position = (0, 0)
        self.goto(self.choose_starting_position())
        self.curr_speed = STARTING_MOVE_DISTANCE

    def choose_starting_position(self):
        starting_y_position = random.randint(-240, 240)
        return (300, starting_y_position)

    def move(self):
        self.goto(self.xcor() - self.curr_speed, self.ycor())
        if self.xcor() < -300:
            self.goto(self.choose_starting_position())

    def increase_speed(self):
        self.curr_speed *= 1.2

