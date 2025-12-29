from turtle import Turtle

TEXT_ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.teleport(0, 280)
        self.color("white")
        self.write(f"Score: {self.score}", align= TEXT_ALIGNMENT, font= FONT)


    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align= TEXT_ALIGNMENT, font= FONT)

    def game_over(self):
        self.teleport(0, 0)
        self.write("Game Over", align= TEXT_ALIGNMENT, font= FONT)