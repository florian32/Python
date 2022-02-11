from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.start()
        self.moving_x = 10
        self.moving_y = 10
        self.color('white')
        self.penup()
        self.shape('circle')

    def start(self):
        self.goto(0, 0)


    def move_right_up(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x + self.moving_x, y + self.moving_y)

    def move_right_down(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x + self.moving_x, y - self.moving_y)

    def move_left_up(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x - self.moving_x, y + self.moving_y)

    def move_left_down(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x - self.moving_x, y - self.moving_y)

    def bounce(self):
        self.moving_y *= -1

    def bounce_paddle(self):
        self.moving_x *= -1

    def new_pos(self):
        self.goto()