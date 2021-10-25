from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        """Creating paddle"""
        self.shape("square")
        self.speed("fastest")
        self.color("white")

        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        """Moves paddle up"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        """Moves paddle down"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
