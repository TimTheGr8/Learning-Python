from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

moveDistance = 10
turnAngle = 10

def move_forward():
    tim.forward(moveDistance)

def move_backward():
    tim.backward(moveDistance)

def turn_left():
    tim.left(turnAngle)

def turn_right():
    tim.right(turnAngle)

def reset():
    tim.reset()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=reset)


screen.exitonclick()