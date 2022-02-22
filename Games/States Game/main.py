import turtle
import pandas
from names import Name
from score import Score
data = pandas.read_csv("50_states.csv")
state_names = data["state"]

game_on = True

answers = Name()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = Score()

while game_on:
    answer_state = screen.textinput(title="Guess the state", prompt="Write a name of a state: ").lower()
    if answer_state == "exit":
        game_on = False
    if len(answers.names) == 50:
        game_on = False

    for state in state_names:
        if state.lower() == answer_state:
            print(data[data["state"] == state])
            x = int(data[data["state"] == state]["x"])
            y = int(data[data["state"] == state]["y"])
            location = (x, y)
            answers.new_name(location, state)
            score.point()


screen.exitonclick()
