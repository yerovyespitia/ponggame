from turtle import Turtle
UP = 30
DOWN = 30


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.goto(x, y)
        self.right(90)
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=5)

    def up(self):
        self.backward(UP)

    def down(self):
        self.forward(DOWN)
