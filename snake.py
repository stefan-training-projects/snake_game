from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0),(-40,0)]
MOVE_DISTANCE = 20
DIRECTIONS = [0, 90, 180, 270]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():

    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.snake_head = self.snake_segments[0]

    def create_snake(self):
        for p in STARTING_POSITIONS:
            sneak_segment = Turtle("square")
            sneak_segment.penup()
            sneak_segment.color('white')
            sneak_segment.goto(p)
            self.snake_segments.append(sneak_segment)

    def move(self):

        for seg_num in range(len(self.snake_segments)-1, 0,-1):
            new_x = self.snake_segments[seg_num-1].xcor()
            new_y = self.snake_segments[seg_num-1].ycor()
            self.snake_segments[seg_num].goto(new_x,new_y)

        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
         if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
