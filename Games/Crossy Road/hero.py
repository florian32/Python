from turtle import Turtle


class Hero(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.setheading(90)
        self.showturtle()
        self.color('white')
        self.starting_pos = (0, -280)
        self.start()

    def start(self):
        self.goto(self.starting_pos)

    def move_up(self):
        y = self.ycor()
        self.goto(self.xcor(), y + 20)

    def move_down(self):
        y = self.ycor()
        self.goto(self.xcor(), y - 20)
