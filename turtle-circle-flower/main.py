import random
from  turtle import  Screen
import turtle as t


tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

directions = [0, 90, 180, 270]
tim.pensize(5)
tim.speed("fastest")

for _ in range(100):
    tim.color(random_color())
    # tim.forward(30)
    # tim.setheading(random.choice(directions))
    tim.circle(100)
    tim.right(10)













screen = Screen()
screen.exitonclick()
