from paddle import Paddle
from turtle import Screen
from ball import Ball
from scoreboard import Scoreboard
import time

# Creating and setting up screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

# Creating needed objects
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
pong_ball = Ball()
score = Scoreboard()

# Implementing key controls
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

screen.onkey(left_paddle.up, "W")
screen.onkey(left_paddle.down, "S")

# Tracking game state
game_is_on = True

# Game logic
while game_is_on:
    time.sleep(pong_ball.ball_speed)
    pong_ball.refresh()
    screen.update()

    # Detect collision with top and bottom screen
    if pong_ball.ycor() > 278 or pong_ball.ycor() < -278:
        pong_ball.bounce_y()

    # Detect collision with paddles
    if pong_ball.distance(right_paddle) < 50 and pong_ball.xcor() > 320 or pong_ball.distance(
            left_paddle) < 50 and pong_ball.xcor() < -320:
        pong_ball.bounce_x()

    # Detect when right paddle misses
    if pong_ball.xcor() > 380:
        pong_ball.reset_position()
        score.l_point()

    # Detect when left paddle misses
    if pong_ball.xcor() < -380:
        pong_ball.reset_position()
        score.r_point()

screen.exitonclick()
