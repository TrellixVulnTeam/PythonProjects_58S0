from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 70, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_r = 0
        self.score_l = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score_l, align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(self.score_r, align=ALIGN, font=FONT)

    def l_point(self):
        self.score_l += 1
        self.update_scoreboard()

    def r_point(self):
        self.score_r += 1
        self.update_scoreboard()
