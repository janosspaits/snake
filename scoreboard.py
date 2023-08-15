from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt", mode="r") as data:
            high_score = data.read()
            self.high_score = int(high_score)
        self.score = 0
        self.pu()
        self.goto(0, 225)
        self.color("darkgreen")
        self.hideturtle()
        self.update_board()

    def update_board(self):
        self.write(f"SCORE: {self.score}  HIGH SCORE: {self.high_score}", move=False, align="center",
                   font=("Courier", 16, "bold"))
        self.goto(0, -240)
        # self.clear()
        self.write(f"USE  W, A, S, D  TO MOVE", move=False, align="center",
                   font=("Courier", 16, "bold"))
        self.goto(0, 225)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 16, "bold"))
    
    def restart_instructions(self):
        self.goto(0, -20)
        self.write("PRESS SPACE TO RESTART", align="center", font=("Courier", 16, "bold"))

    def increase_score(self):
        self.clear()
        self.score += 1
        with open("data.txt", mode="r") as data:
            high_score = int(data.read())
        if self.score > high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        else:
            self.high_score = high_score
        self.update_board()

    def reset_scoreboard(self):
        self.clear()
        self.score = 0
        self.goto(0, 225)
        self.update_board() 


# class Instructions(Scoreboard):
#
#     def __init__(self):
#         super().__init__()
#         self.goto(0, -240)
#         self.clear()
#         self.write(f"USE  W, A, S, D  TO MOVE", move=False, align="center",
#                    font=("Courier", 16, "bold"))
