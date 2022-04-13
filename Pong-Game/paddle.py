from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_position, y_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setposition(x_position, y_position)

    def up(self):
        y_position = self.ycor() + 20
        self.goto(self.xcor(), y_position)

    def down(self):
        y_position = self.ycor() - 20
        self.goto(self.xcor(), y_position)
