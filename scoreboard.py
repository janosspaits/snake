from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.pu()
        self.goto(0, 270)
        self.color("darkgreen")
        self.hideturtle()
        self.update_board()

    def update_board(self):
        self.write(f"SCORE: {self.score}", move=False, align="center", font=("Arial", 18, "bold"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_board()


class Instructions(Scoreboard):

    def __init__(self):
        super().__init__()
        self.goto(0, -290)
        self.clear()
        self.write(f"USE  W, A, S, D  TO MOVE", move=False, align="center",
                   font=("Arial", 18, "bold"))
