from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
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
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with paddles
    if ball.distance(r_paddle) < 48 and r_paddle.xcor() - ball.xcor() < 20 and not ball.xcor() >= r_paddle.xcor():
        ball.bounce_x()
    if ball.distance(l_paddle) < 48 and abs(l_paddle.xcor() - ball.xcor()) < 20 and not ball.xcor() <= l_paddle.xcor():
        ball.bounce_x()
    # Detect if ball went past left paddle
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()
    # Detect if ball went past right paddle
    if  ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()

screen.exitonclick()
