from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(0, 0)
        self.y_move = 10
        self.x_move = 10

    def move(self):
        x_new = self.xcor() + self.x_move
        y_new = self.ycor() + self.y_move
        self.goto(x_new, y_new)

    def v_bounce(self):
        self.y_move *= -1

    def h_bounce(self):
        self.x_move *= -1

    def refresh(self):
        self.goto(0, 0)
        self.x_move *= -2