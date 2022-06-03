from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle_left = Paddle(-350, 0)
paddle_right = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_left.up, "Up")
screen.onkey(paddle_left.down, "Down")
screen.onkey(paddle_right.up, "w")
screen.onkey(paddle_right.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect collision paddle_right
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()

    # Detect collision paddle_left
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()
