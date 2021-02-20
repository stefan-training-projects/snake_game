from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(-40,280)
        self.score = 0
        self.write(f"Score: {self.score} ", False,font=("Verdana", 12, "normal"))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} ", False,font=("Verdana", 12, "normal"))
