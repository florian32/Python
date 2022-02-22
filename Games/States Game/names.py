from turtle import Turtle


class Name:
    def __init__(self):
        self.names = []

    def new_name(self, location, text):
        new = Turtle()
        new.penup()
        new.hideturtle()
        new.color("black")
        new.goto(location)
        new.write(text,align="center")
        self.names.append(new)
