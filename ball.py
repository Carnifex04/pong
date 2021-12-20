import time
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_step = 10
        self.y_step = 10
        self.move_speed = 0.05

    def move(self):
        x_move = self.x_step
        y_move = self.y_step
        self.setposition(self.xcor() + x_move, self.ycor() + y_move)

    def bounce_wall(self):
        self.y_step *= -1

    def l_bounce_paddle(self):
        self.x_step = abs(self.x_step)
        self.move_speed *= 0.8

    def r_bounce_paddle(self):
        self.x_step = -(abs(self.x_step))
        self.move_speed *= 0.8

    def r_misses(self):
        self.setposition(0, 0)
        self.x_step = 10
        self.y_step = 10

    def l_misses(self):
        self.setposition(0, 0)
        self.x_step = -10
        self.y_step = 10

    def reset(self, paddle):
        self.hideturtle()
        self.move_speed = 0.05
        if paddle == "right":
            self.r_misses()
        else:
            self.l_misses()

        self.showturtle()
        time.sleep(1)
