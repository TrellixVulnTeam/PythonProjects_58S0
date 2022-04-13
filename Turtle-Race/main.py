from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y = -100
is_race_on = False


for turtle_color in colors:
    new_turtle = Turtle("turtle")
    new_turtle.color(turtle_color)
    new_turtle.penup()
    new_turtle.goto(x=-200, y=y)
    y += 40
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} is the winner.")
            else:
                print(f"You have lost! The {winning_color} is the winner.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()

