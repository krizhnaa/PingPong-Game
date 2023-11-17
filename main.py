from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()


screen.listen()
screen.onkey(r_paddle.move_up, 'Up')
screen.onkey(r_paddle.move_down, 'Down')
screen.onkey(l_paddle.move_up, 'w')
screen.onkey(l_paddle.move_down, 's')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    if ball.distance(x=ball.xcor(), y=280) < 15 or ball.distance(x=ball.xcor(), y=-280) < 15:
        ball.v_bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.h_bounce()
        print("Made contact")

screen.exitonclick()
