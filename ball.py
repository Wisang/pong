from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.move_speed = 0.1
        self.shape("circle")
        self.color("white")
        self.width = 20
        self.height = 20
        self.penup()
        self.goto(0, 0)
        self.y_step = 10
        self.x_step = 10

    def bounce_y(self):
        self.y_step *= -1

    def bounce_x(self):
        self.x_step *= -1
        self.move_speed *= 0.9

    def move(self):
        new_x = self.xcor() + self.x_step
        new_y = self.ycor() + self.y_step

        self.goto(new_x, new_y)

    def reset_position(self):
        self.bounce_x()
        self.goto(0, 0)
        self.move_speed = 0.1
