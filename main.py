from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

paddle = Paddle()

screen.update()

screen.listen()
screen.onkey(paddle.move_up, 'Up')
screen.onkey(paddle.move_down, 'Down')


screen.exitonclick()
