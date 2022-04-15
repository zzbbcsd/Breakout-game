from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score=0
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.goto(300,350)
        self.write(f"Score:{self.score}", align="center", font=("Courier", 30, "normal"))

    def score_up(self):
        self.score += 1
        self.update_scoreboard()
    def game_over(self):
        new = Turtle()
        new.color("black")
        new.penup()
        new.hideturtle()
        new.goto(0,-100)
        new.write("Game Over", align="center", font=("Courier", 30, "normal"))