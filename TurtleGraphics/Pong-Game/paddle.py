from turtle import Turtle

MOVEMENT = 20
R_PADDLE_X = 350
L_PADDLE_X = -350

class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        # self.create_paddle(side)
        self.shape("square")
        self.color("White")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.teleport(self.pick_side(side), 0)

    def pick_side(self, side):
        if side == "left":
            return L_PADDLE_X
        elif side == "right":
            return R_PADDLE_X
        else:
            print("That is not a valid side!!!!")
            return None
        
    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVEMENT)

    def down(self):
        self.goto(self.xcor(), self.ycor() - MOVEMENT)

