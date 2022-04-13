import turtle
import pandas

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


guessed_states = []


while len(guessed_states) < len(states_list):
    answer_state = screen.textinput(title=f"Guessed: {len(guessed_states)}/{len(states_list)}",
                                    prompt="What's another state name?").title()
    if answer_state in states_list:
        guessed_state = data[data.state == answer_state]
        guessed_states.append(answer_state)
        pin_state = turtle.Turtle()
        pin_state.hideturtle()
        pin_state.penup()
        pin_state.goto(int(guessed_state.x), int(guessed_state.y))
        pin_state.write(answer_state)
    elif answer_state == "End":
        missed_states = [state for state in states_list if state not in guessed_states] # list comprehension
        # for state in states_list:
        #     if state not in guessed_states:
        #         missed_states.append(state)
        data_missed = pandas.DataFrame(missed_states)
        data_missed.to_csv("Missed States.cvs")
        break


screen.exitonclick()