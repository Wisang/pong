import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()

screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

screen.listen()

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))

screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")

screen.onkey(paddle_l.up, "w")
screen.onkey(paddle_l.down, "s")

ball = Ball()
scoreboard = Scoreboard()

screen.tracer(0)

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(paddle_r) < 50 and ball.xcor() > 320) \
            or (ball.distance(paddle_l) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_score += 1
        scoreboard.update_score()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_score += 1
        scoreboard.update_score()
        # is_game_on = False


screen.exitonclick()
