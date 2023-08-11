from turtle import Screen
import time
from snake import Sneki
from food import Food
from scoreboard import Scoreboard, Instructions

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("lightgreen")
screen.title("Sneki snek")
screen.tracer(0)

snake = Sneki()
food = Food()
scoreboard = Scoreboard()
instructions = Instructions()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.09)
    snake.move()

    if snake.head.distance(food) < 17:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 299 or snake.head.xcor() < -299 or snake.head.ycor() > 299 \
        or snake.head.ycor() < -299:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 9:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
