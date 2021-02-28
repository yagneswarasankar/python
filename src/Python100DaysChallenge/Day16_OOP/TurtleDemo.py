# from turtle import Turtle,Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("green","yellow")
# timmy.forward(200)
# timmy.right(90)
# timmy.forward(200)
# timmy.right(90)
# timmy.forward(200)
# timmy.right(90)
# timmy.forward(200)
#
# timmy.left(60)
# timmy.forward(200)
# timmy.right(60)
# timmy.forward(200)
# timmy.left(60)
# timmy.forward(200)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.canvheight = 500
# print(my_screen.canvheight)

# my_screen.exitonclick()
from prettytable import PrettyTable
table  = PrettyTable()

table.add_column("Pokeman Name",["Pikachu","Squirtle","Charmandar"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = "l"
print(table)
