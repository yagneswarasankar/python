import turtle as t
import random
# import colorgram as c
#
# rgb_colors = []
# color = c.colorgram
#
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
#
# colors = color.extract("hirstpainting.jpg",30)

color_list = [(134, 167, 191), (211, 156, 106), (197, 143, 166), (29, 110, 168), (234, 214, 86), (127, 74, 92), (187, 178, 19), (26, 136, 66), (55, 18, 26), (142, 20, 40), (38, 175, 113), (225, 170, 196), (116, 188, 144), (231, 77, 50), (172, 70, 46), (238, 218, 5), (37, 17, 16), (186, 91, 110), (9, 102, 52), (34, 167, 189), (20, 20, 28), (183, 185, 213), (234, 171, 159), (154, 215, 172), (142, 20, 16), (89, 124, 182)]
tim = t.Turtle()
t.colormode(255)

xpos,ypos =-200,-200
def drawhirstpainting(n):
    global xpos,ypos
    tim.penup()
    tim.setposition(xpos , ypos)
    for _ in range(n):
        tim.dot(20,random.choice(color_list))
        tim.forward(50)
    ypos +=50


for _ in range(10):
    drawhirstpainting(10)
    tim.setposition(xpos , ypos)
tim.hideturtle()

my_screen = t.Screen()
my_screen.exitonclick()