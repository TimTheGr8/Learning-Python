from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake(Turtle):
    # Snake setup
    def __init__(self):
        super().__init__()
        self.snake_body = []
        self.create_snake()

    def create_snake(self):
        for s in range(3):
            seg = Turtle(shape="square")
            seg.color("white")
            seg.penup()
            self.snake_body.append(seg)
            seg.goto(self.snake_body[s].xcor() +(s * -20) , self.snake_body[s].ycor())
        
        self.head = self.snake_body[0]

    def add_segment(self):
        seg = Turtle(shape="square")
        seg.color("white")
        seg.penup()
        self.snake_body.append(seg)

    def move(self):
        for body_segment in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[body_segment - 1].xcor()
            new_y = self.snake_body[body_segment - 1].ycor()
            self.snake_body[body_segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.snake_body:
            seg.goto(1000,1000)
        
        self.snake_body.clear()
        self.create_snake()
