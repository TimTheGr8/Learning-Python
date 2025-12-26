import turtle as t
from turtle import Screen

tim = t.Turtle()

tim.shape("turtle")
tim.color("chartreuse")
# Draw a square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
tim.penup()
# tim.backward(500)
# Draw dashed line 10 paces on 10 paces off for 50 times
tim.pos()
for _ in range(15):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)

print("Done drawing!")
screen = Screen()
screen.exitonclick()