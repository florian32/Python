import random
from turtle import Turtle

COLORS = ["red", "orange", "white", "green", "blue", "purple"]

class Cars:
    def __init__(self):
        y = -200
        self.starting_x = 450
        self.speed = 2
        self.los = [0, 0, 0, 0, 0]
        self.distances = [200, 100, 150, 250, 50]
        self.lines = []

        for i in range(5):
            self.lines.append([])

        for line in self.lines:
            self.new_turtle((self.starting_x, y), line)
            y += 100

    def new_turtle(self, position, tab):
        new = Turtle()
        new.shape('square')
        new.color(random.choice(COLORS))
        new.penup()
        new.shapesize(stretch_wid=1, stretch_len=3)
        new.goto(position)
        tab.append(new)

    def move(self):

        global distance
        index = 0
        for line in self.lines:
            if self.los[index] == 0:
                self.distances[index] = random.randint(0, 300)
                self.los[index] = 1

            if self.los[index] == 1:
                if line[-1].xcor() < self.distances[index]:
                    position = (self.starting_x, line[-1].ycor())
                    self.new_turtle(position, line)
                    self.los[index] = 0

            for car in line:
                x = car.xcor()
                car.goto(x - self.speed, car.ycor())

            if line[0].xcor() < -450:
                del line[0]
            index += 1

    def next_level(self):
        self.speed += 0.5

