from turtle import Turtle

FONT = ("Courier", 12, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0
        with open('data.txt') as file:
            self.high_score = int(file.read())

        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(-80,280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score} ",font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open('data.txt',mode='w') as file:
            contents = str(self.high_score)
            file.write(contents)
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()



