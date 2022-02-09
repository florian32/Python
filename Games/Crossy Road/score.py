from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, ):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0, 250)
        self.score = 0
        self.write(f"Level 1", False, align='center', font=('Arial', 16, 'normal'))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over your score is {self.score}", False, align='center', font=('Arial', 24, 'normal'))

    def next(self):
        self.goto(0, 250)
        self.score += 1
        self.clear()
        self.write(f"Level {self.score}", False, align='center', font=('Arial', 16, 'normal'))

    def wait(self):
        self. goto(0, 0)
        self.write(f"Wait", False, align='center', font=('Arial', 24, 'normal'))
