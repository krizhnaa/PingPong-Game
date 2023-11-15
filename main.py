from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Pong')

paddle = Paddle()



screen.exitonclick()