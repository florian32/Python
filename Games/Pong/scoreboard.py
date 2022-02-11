from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.score_right = 0
        self.score_left = 0
        self.goto(0, 270)

    def start(self):
        self.clear()
        self.write(f"Left {self.score_left}    vs    Right {self.score_right}", align='center', font=('Arial', 16, 'normal'))

    def score_up_left(self):
        self.score_left += 1

    def score_up_right(self):
        self.score_right += 1
