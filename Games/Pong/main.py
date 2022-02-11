import random
from turtle import Turtle, Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)
scoreboard = Scoreboard()

game_on = True

left = Paddle((-380, 0))
right = Paddle((380, 0))
ball = Ball()

screen.listen()
screen.onkeypress(left.move_up, 'w')
screen.onkeypress(left.move_down, 's')
screen.onkeypress(right.move_up, 'Up')
screen.onkeypress(right.move_down, 'Down')

scoreboard.start()
while game_on:
    time.sleep(0.03)
    screen.update()
    ball.move_right_up()
    left_pos = (left.ycor() - 50, left.ycor() + 50)
    right_pos = (right.ycor() - 50, right.ycor() + 50)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.xcor() > 360 and right_pos[0] < ball.ycor() < right_pos[1]:
        ball.bounce_paddle()

    if ball.xcor() < -360 and left_pos[0] < ball.ycor() < left_pos[1]:
        ball.bounce_paddle()

    if ball.xcor() > 390:
        scoreboard.score_up_right()
        scoreboard.start()
        time.sleep(1)
        ball.start()

    if ball.xcor() < -390:
        scoreboard.score_up_left()
        scoreboard.start()
        time.sleep(1)
        ball.start()


screen.exitonclick()
