from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
xStart = -240
yDim = 100
colors = ["blue", "orange", "purple", "red", "green"]

turtles = []

for i in range(5):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].color([colors[i]])
    turtles[i].penup()
    turtles[i].goto(xStart, yDim)
    yDim -= 50

user__bet = screen.textinput(title="Place your bet", prompt="Which turtle do you think will win the race? Enter a color:").lower()

racing = True
winner = ""
while racing:
    for turtle in turtles:
        turtle.forward(random.randint(0, 12))
        if turtle.xcor() >= 230:
            racing = False
            winner = turtle.fillcolor().title()

print(f"{winner} turtle is the winner!")

screen.exitonclick()
