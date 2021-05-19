from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_c_clockwise():
    tim.circle(50, 100)

def move_clockwise():
    tim.circle(- 50, 100)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_c_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="x", fun=turn_left)
screen.onkey(key="c", fun=turn_right)
screen.onkey(key="z", fun=clear)
screen.exitonclick()

