from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.title("PyPong")
screen.tracer(0)
root = screen._root
root.iconbitmap("TurtleGraphics/Pong-Game/ping-pong.ico")

r_paddle = Paddle("right")
l_paddle = Paddle("left")
ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    # Detect collision with paddles
    if ball.distance(r_paddle) < 48 and r_paddle.xcor() - ball.xcor() < 20 and not ball.xcor() >= r_paddle.xcor():
        ball.ricochet()
    if ball.distance(l_paddle) < 48 and abs(l_paddle.xcor() - ball.xcor()) < 20 and not ball.xcor() <= l_paddle.xcor():
        ball.ricochet()


screen.exitonclick()
