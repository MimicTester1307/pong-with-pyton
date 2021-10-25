from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the scores displayed on the screens"""
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))

    def l_point(self):
        """Controls the increment of the left paddle's score"""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Controls the increment of the right paddle's score"""
        self.r_score += 1
        self.update_scoreboard()
