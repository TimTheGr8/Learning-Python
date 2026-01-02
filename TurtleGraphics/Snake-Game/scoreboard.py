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
        self.high_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align= TEXT_ALIGNMENT, font= FONT)

    def add_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.teleport(0, 0)
        self.write("Game Over", align= TEXT_ALIGNMENT, font= FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
