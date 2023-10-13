from turtle import *
import random

screen = Screen()
screen.setup(500, 400)
is_race_on = False
user_input = screen.textinput("Turtle Race", "Which turtle will win? Choose the colour: ")
colors = ["red", "blue", "yellow", "green", "pink", "purple"]
y_length = -120

all_turtles = []

for i in range(6):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.color(colors[i])
    new_turtle.goto(-230, y_length)
    y_length += 40
    all_turtles.append(new_turtle)

if user_input:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on=False
            winning_turtle = turtle.pencolor()
            if user_input == winning_turtle:
                print(f"You've Won the race. The {winning_turtle} has won the race")
            else:
                print(f"You've Lost the race. The {winning_turtle} has won the race")

        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
