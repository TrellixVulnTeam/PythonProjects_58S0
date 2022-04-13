from turtle import Turtle
import random
colors = ["red", "blue", "green", "pink", "yellow"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # from 20, 20 px to 10, 10 px
        self.change_color()
        self.refresh()

    def refresh(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)

    def change_color(self):
        self.color(random.choice(colors))
