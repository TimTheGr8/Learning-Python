from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("white")
        self.speed(0)
        self.refresh()

    def refresh(self):
        rand_y = random.randint(-260, 260)
        rand_x = random.randint(-260, 260)
        self.teleport(rand_x, rand_y)
