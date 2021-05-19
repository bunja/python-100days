from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle win the race? Enter a color")
color = ["red", "orange", "yellow", "green", "blue", "violet"]
y = -100
all_turtles = []
for i in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(color[i])
    new_turtle.penup()
    y = y + 30
    new_turtle.goto(x=-230, y = y)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you won {winning_color}")
            else:
                print(f"you lost {winning_color}")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()


