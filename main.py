from turtle import Turtle, Screen
import turtle
import pandas

screen = Screen()
# screen.bgpic("blank_states_img.gif")

image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

timmy = Turtle()
timmy.hideturtle()

is_on = True

data = pandas.read_csv("50_states.csv")

list_state = data["state"].to_list()
list_x = data["x"].to_list()
list_y = data["y"].to_list()

print(list_state)

score = 0
guessed_states = []
missed_states = []

while is_on and score <50:
    state = screen.textinput(title=f"State game {score}/50", prompt="enter another state: (enter 'exit' to exit)").title()
    if state == "Exit":
        for state in list_state:
            if state not in guessed_states:
                missed_states.append(state)
        dict = {"states":missed_states}
        df = pandas.DataFrame(dict)
        df.to_csv("states_to_learn.csv")
        break
    if state in list_state:
        index = list_state.index(state)
        timmy.penup()
        timmy.goto(list_x[index], list_y[index])
        timmy.pendown()
        timmy.write(state, align="center", font=("Arial", 8, "normal"))
        score += 1
        guessed_states.append(state)






screen.exitonclick()