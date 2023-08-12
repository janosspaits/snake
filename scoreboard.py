from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.pu()
        self.goto(0, 225)
        self.color("darkgreen")
        self.hideturtle()
        self.update_board()

    def update_board(self):
        self.write(f"SCORE: {self.score}", move=False, align="center", font=("Courier", 16, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 16, "bold"))
    
    def restart_instructions(self):
        self.goto(0, -20)
        self.write("PRESS SPACE TO RESTART", align="center", font=("Courier", 16, "bold"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_board()

    def reset(self):
        self.clear()
        self.score = 0
        self.goto(0, 225)
        self.update_board() 

class Instructions(Scoreboard):

    def __init__(self):
        super().__init__()
        self.goto(0, -240)
        self.clear()
        self.write(f"USE  W, A, S, D  TO MOVE", move=False, align="center",
                   font=("Courier", 16, "bold"))
