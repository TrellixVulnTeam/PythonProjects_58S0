import turtle as t
import random
from turtle import Screen
# import colorgram
#
rgb_colors = []
# colors = colorgram.extract('hirst_colors.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

print(rgb_colors)
color_list = [(194, 166, 108), (135, 167, 193), (49, 102, 145), (145, 90, 43), (10, 21, 54), (188, 156, 34),
(224, 208, 115), (62, 23, 10), (184, 141, 165), (69, 119, 79), (59, 13, 24), (138, 180, 149), (135, 28, 13),
(129, 77, 104), (14, 41, 25),
 (19, 53, 135), (120, 27, 42), (169, 101, 135), (94, 152, 97), (176, 188, 217),
 (88, 121, 182), (181, 100, 88), (22, 92, 65), (68, 152, 169), (210, 177, 202), (88, 77, 15)]


ana = t.Turtle()
t.colormode(255)
ana.penup()
ana.setx(-250)
ana.sety(-220)


def row_color():
    ana.pendown()
    for _ in range(10):
        random_color = random.choice(color_list)
        ana.dot(20, random_color)
        ana.penup()
        ana.forward(50)
    ana.penup()
    ana.left(90)
    ana.forward(50)
    ana.left(90)
    ana.forward(500)
    ana.left(180)


for times in range(10):
    row_color()


screen = Screen()
screen.exitonclick()

# ana.left(90)
# ana.begin_fill()
# ana.circle(80)
# ana.end_fill()

# for times in range (0, 10):
#     ana.penup()
#     ana.forward(10)
#     ana.pendown()
#     ana.forward(10)



