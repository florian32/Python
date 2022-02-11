from turtle import Turtle

POSITION_LEFT = (-380, 0)
POSITION_RIGHT = (380, 0)


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.starting_pos = position
        self.penup()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(position)

    def move_up(self):
        y = self.ycor()
        self.goto(self.xcor(), y + 20)

    def move_down(self):
        y = self.ycor()
        self.goto(self.xcor(), y - 20)
