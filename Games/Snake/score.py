from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, ):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        with open("Data.txt", mode='r') as file:
            self.high_score = int(file.read())
        self.write(f"Your score is 0    high score is {self.high_score}", False, align='center',
                   font=('Arial', 16, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Data.txt", mode='w') as file:
                file.write(f"{self.score}")
        self.score = 0
        self.update_score()

    def next(self):
        self.score += 1
        self.clear()
        self.write(f"Your score is {self.score}    high score is {self.high_score}", False, align='center',
                   font=('Arial', 16, 'normal'))

    def update_score(self):
        self.clear()
        self.write(f"Your score is {self.score}    high score is {self.high_score}", False, align='center',
                   font=('Arial', 16, 'normal'))
