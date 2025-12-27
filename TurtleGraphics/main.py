import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
screen = Screen()

screen.colormode(255)
tim.shape("triangle")
tim.shapesize(1,1)
moveDirection = [0, 90, 180, 270]
totalLines = random.randint(100, 300)

def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.pencolor((r, g, b))
    tim.fillcolor((r, g, b))

def choose_direction():
    tim.setheading(random.choice(moveDirection))

# Draw a square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# Draw dashed line 10 paces on 10 paces off for 15 times
# tim.pos()
# for _ in range(15):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)

# Draw traingle, square, pentagon, hexagon, hepagon, octogon, nonogon, decogon 
# 360 divide by number of sides
# for numberOfSides in range(3, 11):
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     tim.pencolor((r, g, b))
#     tim.fillcolor((r, g, b))
#     angle = 360 / numberOfSides
#     for _ in range(numberOfSides):
#         tim.forward(100)
#         tim.right(angle)

# Draw a random walk
tim.speed(0)
tim.pensize(10)
lines = 0
while lines < totalLines:
    choose_direction()
    rand_color()
    tim.forward(25)
    lines += 1



screen.exitonclick()