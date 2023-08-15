from turtle import Screen
import time
from snake import Sneki
from food import Food
from scoreboard import Scoreboard  # Instructions

speed = 0.1


def start_game():
    global speed
    snake.reset()
    food.refresh()
    scoreboard.reset_scoreboard()
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(speed)
        snake.move()

        if snake.head.distance(food) < 8:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()
            if scoreboard.score % 3 == 0:
                speed *= 0.8

        if snake.head.xcor() > 248 or snake.head.xcor() < -248 or snake.head.ycor() > 248 \
                or snake.head.ycor() < -248:
            game_is_on = False
            scoreboard.game_over()
            scoreboard.restart_instructions()
            speed = 0.1

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 9:
                game_is_on = False
                scoreboard.game_over()
                scoreboard.restart_instructions()
                speed = 0.1


screen = Screen()

screen.setup(500, 500)
screen.bgcolor("lightgreen")
screen.title("Sneki snek")
screen.tracer(0)

snake = Sneki()
food = Food()
scoreboard = Scoreboard()
# instructions = Instructions()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
screen.onkey(start_game, "space")  # restart the game when space is pressed

start_game()

screen.exitonclick()
