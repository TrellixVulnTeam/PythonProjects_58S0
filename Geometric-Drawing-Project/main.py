from turtle import Screen
import random
import turtle as t


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


ana = t.Turtle()
t.colormode(255)
ana.speed(70)

#
# ana.pensize(7)
# # nr_of_sides = 3
# colors = ["pink", "royal blue", "yellow green", "khaki", "thistle", "coral", "red", "dark slate blue"]
#
#
# def draw(nr_sides):
#     angle = 360 / nr_sides
#     for times in range(nr_sides):
#         ana.forward(100)
#         ana.right(angle)
# def draw_spiral():
#     angle = 360 / 36
#     for times in range(0, 36):
#         ana.color(random_color())
#         ana.circle(60)
#         ana.left(angle)
#
# draw_spiral()

#
#
# for times_draw in range(0, 8):
#     ana.color(random.choice(colors))
#     draw(nr_of_sides)
#     nr_of_sides += 1

# ana.left(90)
# ana.begin_fill()
# ana.circle(80)
# ana.end_fill()

# for times in range (0, 10):
#     ana.penup()
#     ana.forward(10)
#     ana.pendown()
#     ana.forward(10)


# direction = [0, 90, 180, 270]
# left_right = ["left", "right"]

# for times in range(0, 200):
#     ana.forward(20)
#     ana.color(random_color())
#     ana.setheading(random.choice(direction))

def draw_spirograpf(angle):
    for _ in range(int(360 / angle)):
        ana.color(random_color())
        ana.circle(100)
        ana.setheading(ana.heading() + angle)


draw_spirograpf(5)


screen = Screen()
screen.exitonclick()


