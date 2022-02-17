from turtle import Turtle, Screen
import random

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win?")
bet.lower()
y = -150
race = False
turtles = []

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(-235, y)
    y += 50
    turtles.append(new_turtle)

if bet != '':
    race = True

while race:
    for turtle in turtles:

        if turtle.xcor() > 210:
            winner = turtle
            race = False

        pace = random.randint(1, 10)
        turtle.forward(pace)

print(f"The winner is the {winner.color()[0]} turtle\n")
if bet == winner.color()[0]:
    print('You have won')
else:
    print("You have lost")

screen.exitonclick()
