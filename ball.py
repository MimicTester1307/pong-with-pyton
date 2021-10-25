from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super(Ball, self).__init__()
        self.y_move = 10
        self.x_move = 10
        self.create_ball()
        self.ball_speed = 0.1

    def create_ball(self):
        """Creates the ball"""
        self.color("white")
        self.shape("circle")
        self.penup()
        self.speed("normal")

    def refresh(self):
        """Changes the position of the ball (moves it)"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Controls the bouncing of the ball when it hits the top or bottom screen"""
        self.y_move *= -1

    def bounce_x(self):
        """Controls the bouncing of the ball when it hits a paddle"""
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        """Resets the position of the ball"""
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_x()
