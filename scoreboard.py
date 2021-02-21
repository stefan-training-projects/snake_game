from turtle import Turtle

FONT = ("Courier", 12, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0
        self.high_score = 0

        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(-40,280)
        self.update_score()

    # def game_over(self):
    #     self.goto(-40,0)
    #     self.write("GAME OVER.", font=FONT)


    def update_score(self):
        self.clear()
        self.score += 1
        self.goto(-80,280)
        self.write(f"Score: {self.score} High Score: {self.high_score} ",font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()


