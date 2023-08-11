from turtle import Screen # Turtle
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
    time.sleep(0.2)
    snake.move()

    if snake.head.distance(food) < 17:
        food.refresh()
        scoreboard.increase_score()

screen.exitonclick()
