import turtle
import pandas

screen = turtle.Screen()
screen.setup(800, 600)
screen.title("State Guessing Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []

# detecting x and y values
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Correct", prompt="What's another state name?").title()
    # answer_state = 'Alabama'
    data = pandas.read_csv("50_states.csv")
    states = data['state'].to_list()
    # print(states)
    if answer_state == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        data = pandas.DataFrame(missing_states)
        data.to_csv("states_to_learn.csv")
        break
    if answer_state in states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
# states to learn

screen.exitonclick()
