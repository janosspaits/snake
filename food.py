from turtle import Turtle, Screen
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("maroon")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.choice(range(-280, 280, 20))
        random_y = random.choice(range(-280, 280, 20))
        self.goto(random_x, random_y)

