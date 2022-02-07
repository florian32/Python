from turtle import Turtle
import random

RANGE = []
for i in range(-260, 260, 20):
    RANGE.append(i)


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('white')
        self.speed('fastest')
        self.go()

    def go(self):
        random_x = random.choice(RANGE)
        random_y = random.choice(RANGE)
        self.goto(random_x, random_y)
