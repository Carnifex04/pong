from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")

left_paddle = Paddle(-385)
right_paddle = Paddle(380)

ball = Ball()

scoreboard = Scoreboard()

screen.tracer(0)

screen.listen()
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(left_paddle.move_down, "s")
screen.onkeypress(right_paddle.move_down, "Down")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # collision with the upper or lower wall
    if ball.ycor() > 280 or ball.ycor() < -285:
        ball.bounce_wall()

    # collision with the paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 350:
        ball.r_bounce_paddle()

    if ball.distance(left_paddle) < 50 and ball.xcor() < -355:
        ball.l_bounce_paddle()

    # right paddle misses
    if ball.xcor() > 380:
        ball.reset("right")
        left_paddle.reset((-385, 0))
        right_paddle.reset((380, 0))
        scoreboard.l_point()

    # left paddle misses
    if ball.xcor() < -388:
        ball.reset("left")
        left_paddle.reset((-385, 0))
        right_paddle.reset((380, 0))
        scoreboard.r_point()

screen.exitonclick()
