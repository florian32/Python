from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Scoreboard

game_is_on = True

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)

while game_is_on:
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        snake.new()
        food.go()
        score.next()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 or snake.collision() == True:
        score.reset()
        snake.reset()


    screen.update()

screen.exitonclick()



