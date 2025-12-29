from turtle import Turtle

FONT = ("Courier", 80, "normal")
TEXT_ALIGNMENT = "center"
L_SCORE_POSITION = (-100, 180)
R_SCORE_POSITION = (100, 180)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(L_SCORE_POSITION)
        self.write(self.l_score, align=TEXT_ALIGNMENT, font=FONT)
        self.goto(R_SCORE_POSITION)
        self.write(self.r_score, align=TEXT_ALIGNMENT, font=FONT)
    
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

