from turtle import Turtle, Screen
import time
import random
from hero import Hero
from cars import Cars
from score import Scoreboard
game_on = True
screen = Screen()
screen.bgcolor('black')
screen.tracer(0)
screen.setup(width=800, height=600)
screen.listen()
turtle = Hero()

scoreboard = Scoreboard()
scoreboard.wait()
car = Cars()
timeout = time.time() + 4
while True:
    time.sleep(0.001)
    car.move()
    screen.update()
    if time.time() > timeout:
        scoreboard.next()
        break

screen.onkey(turtle.move_up, 'Up')
screen.onkey(turtle.move_down, 'Down')

while game_on:
    time.sleep(0.001)
    car.move()
    screen.update()
    turtle_x = turtle.xcor()
    turtle_y = turtle.ycor()
    for line in car.lines:
        for carly in line:
            if carly.xcor() - 42 < turtle_x < carly.xcor() + 42 and carly.ycor() - 30 < turtle_y < carly.ycor() + 30:
                scoreboard.game_over()
                game_on = False

    if turtle.ycor() > 250:
        turtle.goto(turtle.starting_pos)
        car.next_level()
        scoreboard.next()


screen.exitonclick()
