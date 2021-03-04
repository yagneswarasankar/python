from turtle import Turtle,Screen
import random

my_screen = Screen()
my_screen.setup(height = 400,width=500)
user_bet = my_screen.textinput(title="Make you bet",prompt="Which turtle will win : Enter color")
turtle_colors = ["red","orange","yellow","blue","green","purple"]
turtle_objects =[]
turtle_names = ["tam","tem","tim","tom","tum"]
turtle_passes = range(11)
y = -100
i = 0
for _  in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_colors[i])
    turtle_objects.append(new_turtle)
    i = i + 1
    new_turtle.penup()
    new_turtle.goto(-230,y)
    y = y + 30

if user_bet:
    is_run_on = True
while is_run_on:
    for turtle in turtle_objects:
        if turtle.xcor() > 230:
            is_run_on = False
            winning_turtle_color = turtle.pencolor()
            if(winning_turtle_color == user_bet):
                print(f"You've one and {winning_turtle_color} turtle won!")
            else:
                print(f"You lost. {winning_turtle_color} won! ")

        turtle.forward(random.randint(0,10))
my_screen.exitonclick()