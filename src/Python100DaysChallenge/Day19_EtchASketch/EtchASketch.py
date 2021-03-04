import  turtle as t
from turtle import Screen

tim = t.Turtle()
my_screen = t.Screen()


def moveforward():
    tim.forward(10)

def movebackward():
    tim.backward(10)

def moveleft():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def moveright():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()



my_screen.listen()

my_screen.onkey(fun=moveforward,key = "W".lower())
my_screen.onkey(fun=movebackward,key = "S".lower())
my_screen.onkey(fun=moveleft,key = "A".lower())
my_screen.onkey(fun=moveright,key = "D".lower())
my_screen.onkey(fun=clear,key = "C".lower())

my_screen.exitonclick()