from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 350)
        self.write(f"Your score is {self.score}/50", font="Calibre", align="center")

    def point(self):
        self.clear()
        self.score += 1
        self.write(f"Your score is {self.score}/50", font="Calibre", align="center")
