from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-10, 0), (-20, 0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Sneki:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.direction_change = 0

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("black")
        new_segment.shapesize(0.5, 0.5)
        new_segment.pu()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        self.direction_change = 0
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT and self.direction_change < 1:
            self.head.setheading(RIGHT)
            self.direction_change += 1
 
    def left(self):
        if self.head.heading() != RIGHT and self.direction_change < 1:
            self.head.setheading(LEFT)
            self.direction_change += 1
 
    def up(self):
        if self.head.heading() != DOWN and self.direction_change < 1:
            self.head.setheading(UP)
            self.direction_change += 1
 
    def down(self):
        if self.head.heading() != UP and self.direction_change < 1:
            self.head.setheading(DOWN)
            self.direction_change += 1

    def reset(self):
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.head.setheading(RIGHT)
