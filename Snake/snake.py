from turtle import Turtle

MOVING_DISTANCE = 20
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.start()
        self.head = self.segments[0]

    def start(self):
        for i in STARTING_POS:
            new = Turtle(shape='square')
            new.color('white')
            new.penup()
            new.goto(i)
            self.segments.append(new)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            newx = self.segments[seg - 1].xcor()
            newy = self.segments[seg - 1].ycor()
            self.segments[seg].goto(newx, newy)

        self.head.forward(MOVING_DISTANCE)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def new(self):
        heading = self.segments[len(self.segments) - 1].heading()
        pos_x = self.segments[len(self.segments) - 1].xcor()
        pos_y = self.segments[len(self.segments) - 1].ycor()
        new = Turtle(shape='square')
        new.color('white')
        new.penup()
        self.segments.append(new)

        if heading == 0:
            new.goto(pos_x - 20, pos_y)
        elif heading == 90:
            new.goto(pos_x, pos_y - 20)
        elif heading == 180:
            new.goto(pos_x + 20, pos_y - 20)
        elif heading == 270:
            new.goto(pos_x, pos_y + 20)

    def collision(self):
        for index in range(1,len(self.segments) - 1):
            if self.head.distance(self.segments[index]) < 5:
                return True
        return False

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.start()
        self.head = self.segments[0]

