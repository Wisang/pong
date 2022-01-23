from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.width = 20
        self.height = 20
        self.penup()
        self.goto(0,0)
        self.y_dir = 1

    def move(self):
        if self.ycor() > 280:
            self.y_dir = -1
        elif self.ycor() < -280:
            self.y_dir = 1

        new_x = self.xcor() + 10
        new_y = self.ycor() + self.y_dir * 10
        self.goto(new_x, new_y)