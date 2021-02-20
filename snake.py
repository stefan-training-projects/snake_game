from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0),(-40,0)]

class Snake():

    def __init__(self):
        self.sneak_segments = []
        self.create_snake()

    def create_snake(self):
        for p in STARTING_POSITIONS:
            sneak_segment = Turtle("square")
            sneak_segment.penup()
            sneak_segment.color('white')
            sneak_segment.goto(p)
            self.sneak_segments.append(sneak_segment)

    def move(self):

        for seg_num in range(len(self.sneak_segments)-1, 0,-1):
            new_x = self.sneak_segments[seg_num-1].xcor()
            new_y = self.sneak_segments[seg_num-1].ycor()
            self.sneak_segments[seg_num].goto(new_x,new_y)

        self.sneak_segments[0].forward(20)