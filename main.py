from turtle import Screen
from snake import Snake
import time

#screen details
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Sneky Snek')
screen.tracer(0)

snake = Snake()

game_is_on = True

#move sneak
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()



screen.exitonclick()