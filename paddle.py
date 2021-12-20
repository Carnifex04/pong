from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_coord):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.setposition(x=x_coord, y=0)

    def move_up(self):
        self.setposition(x=self.xcor(), y=self.ycor() + 20)

    def move_down(self):
        self.setposition(x=self.xcor(), y=self.ycor() - 20)

    def reset(self, position):
        self.setposition(position)
