from turtle import Screen, Turtle
import time

#screen details
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Sneky Snek')
screen.tracer(0)

#create snek initial body

starting_position = [(0,0), (-20,0),(-40,0)]

sneak_segments = []

for p in starting_position:
    sneak_segment = Turtle("square")
    sneak_segment.penup()
    sneak_segment.color('white')
    sneak_segment.goto(p)
    sneak_segments.append(sneak_segment)


game_is_on = True

#move sneak
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(sneak_segments)-1, 0,-1):
        new_x = sneak_segments[seg_num-1].xcor()
        new_y = sneak_segments[seg_num-1].ycor()

    sneak_segments[0].forward(20)



screen.exitonclick()