from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# screen details
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Sneky Snek")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()


# snake key commands
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

# move sneak
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision between snake and food
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update_score()

    # Detect collision with wall
    if (
        snake.snake_head.xcor() > 290
        or snake.snake_head.xcor() < -290
        or snake.snake_head.ycor() > 290
        or snake.snake_head.ycor() < -290
    ):
        game_is_on = False
        score.game_over()

    #Detect collision with tail
    for segment in snake.snake_segments:
        if segment == snake.snake_head:
            pass
        elif snake.snake_head.distance(segment) < 10:
            game_is_on = False
            score.game_over()



screen.exitonclick()
