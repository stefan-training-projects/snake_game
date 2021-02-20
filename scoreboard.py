from turtle import Turtle

FONT = ("Courier", 12, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(-40,280)
        self.score = 0
        self.write(f"Score: {self.score} ",font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER.", font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} ",font=FONT)
