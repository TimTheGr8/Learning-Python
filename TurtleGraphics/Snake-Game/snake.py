from turtle import Turtle

MOVE_DISTANCE = 20

class Snake:
    # Snake setup
    def __init__(self):
        self.snake_body = []
        self.create_snake()

    def create_snake(self):
        for s in range(3):
            seg = Turtle(shape="square")
            seg.color("white")
            seg.penup()
            self.snake_body.append(seg)
            seg.goto(self.snake_body[s].xcor() +(s * -20) , self.snake_body[s].ycor())

    def move(self):
        for body_segment in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[body_segment - 1].xcor()
            new_y = self.snake_body[body_segment - 1].ycor()
            self.snake_body[body_segment].goto(new_x, new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)
