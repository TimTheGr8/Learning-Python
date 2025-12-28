from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("PySnake")
screen.tracer(0)
update_delay = 0.15

scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left") 
screen.onkey(snake.right, "Right")

# Game logic    
game_running = True
while game_running:
    snake.move()
    screen.update()
    time.sleep(update_delay)

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        # snake.add_segment()
        scoreboard.add_score()

