# import colorgram
# colors = colorgram.extract("TurtleGraphics/HirstPainting/hirst-pallette.jpg", 15)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     hirst_colors.append((r, g, b))

# print(hirst_colors)

import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
screen = Screen()

screen.colormode(255)
tim.shape("triangle")
tim.shapesize(0.75, 0.75)
tim.hideturtle()
tim.penup()
tim.speed(0)

xBounds = -460
yBounds = -380

hirst_colors = [(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251)]

def random_color():
    return random.choice(hirst_colors)

def move():
    if tim.xcor() >= abs(xBounds):
        tim.teleport(xBounds, tim.ycor() + 50)
    else:
        tim.forward(50)

def draw_dot():
    newColor = random_color()
    tim.dot(20, newColor)

tim.teleport(xBounds, yBounds)
while tim.ycor() < abs(yBounds):
    draw_dot()
    move()


print("Painting done!")
# Draw dot 20 in size spaced 50 apart 810 h x 960 w
screen.exitonclick()