from turtle import Screen, Turtle
import pandas as pd

screen = Screen()
screen.title("U.S. States Game")

img = "US-States-Game/blank_states_img.gif"
screen.addshape(img)

tim = Turtle(shape=img)
name_turtle = Turtle()
name_turtle.penup()
name_turtle.hideturtle()
tim.penup()

state_data = pd.read_csv("US-States-Game/50_states.csv")
all_states = state_data.state.to_list()
correct_states = []

while len(correct_states) < len(all_states):
    state_guess = screen.textinput(f"{len(correct_states)}/50 States Correct", "Name a state on the map").title()

    if state_guess == "Exit":
        break
    elif state_guess in all_states and state_guess not in correct_states:
        curr_state = state_data[state_data.state == state_guess]
        name_turtle.goto(curr_state.x.item(), curr_state.y.item())
        name_turtle.write(curr_state.state.item())
        correct_states.append(state_guess)
    screen.tracer(1)

# screen.mainloop()
# states_to_learn.csv
states_to_learn = []
for state in all_states:
    if state not in correct_states:
        states_to_learn.append(state)

df = pd.DataFrame(states_to_learn)
df.to_csv("US-States-Game/state_to_learn.csv")