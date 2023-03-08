from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(500, 400)
guess = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Place your bet!")
race_start = False

colors = ["red", "blue", "yellow", "green", "orange", "violet"]
turtles = []
n = 0
for i in range(0, 6):
    j = i
    i = Turtle(shape="turtle")
    turtles.append(i)
    turtles[j].penup()
    turtles[j].color(colors[j])
    turtles[j].goto(x=-230, y=-100 + n)
    turtles[j].speed(0)
    n += 40

if guess:
    race_start = True

while race_start:
    for i in range(0, 6):
        spd = random.randint(0, 10)
        turtles[i].forward(spd)
        if turtles[i].xcor() >= 190:
            race_start = False
            winner = turtles[i]

if guess == winner.color()[1]:
    print(f"The {guess} turtle won! Congrats!!!")
else:
    print(f"The {winner.color()[1]} turtle won! You lost your bet unfortunately!")
screen.exitonclick()
