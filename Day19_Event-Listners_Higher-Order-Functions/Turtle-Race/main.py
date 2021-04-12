from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(height=400, width=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which color turtle will win the race: ")
colors = ["red", "orange", "purple", "green", "blue"]
y_positions = [-100, -50, 0, 50, 100]
all_turtles = []

for i in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-240, y=y_positions[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Won!!! {winning_color} turtle won")

            else:
                print(f"You Lost. {winning_color} turtle won")
        random_distance = randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
