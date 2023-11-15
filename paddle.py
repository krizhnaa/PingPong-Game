from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('square')
        # self.turtlesize(stretch_wid=20, stretch_len=100)
        self.goto(250, 0)
