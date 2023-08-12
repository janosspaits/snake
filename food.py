from turtle import Turtle, Screen
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=0.4, stretch_wid=0.4)
        self.color("maroon")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.choice(range(-230, 230, 10))
        random_y = random.choice(range(-230, 230, 10))
        self.goto(random_x, random_y)

