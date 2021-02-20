from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0),(-40,0)]
MOVE_DISTANCE = 20
DIRECTIONS = [0, 90, 180, 270]

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

        self.sneak_segments[0].forward(MOVE_DISTANCE)

    def up(self):
        self.sneak_segments[0].setheading(90)

    def down(self):
        self.sneak_segments[0].setheading(270)

    def left(self):
        self.sneak_segments[0].setheading(180)

    def right(self):
        self.sneak_segments[0].setheading(0)