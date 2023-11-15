from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(0, 0)

    def move(self):
        x_new = self.xcor() + 10
        y_new = self.ycor() + 10
        self.goto(x_new, y_new)