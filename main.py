import time
from turtle import Screen, Turtle

from ball import Ball
from paddle import Paddle

screen = Screen()

screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

screen.listen()

paddle_r = Paddle((350, 0))
Paddle_l = Paddle((-350, 0))

screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")

screen.onkey(Paddle_l.up, "w")
screen.onkey(Paddle_l.down, "s")

ball = Ball()

screen.tracer(0)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.05)
    ball.move()


screen.exitonclick()