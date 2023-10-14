import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.color("blue")
        x_side = random.randint(-280, 280)
        y_side = random.randint(-280, 280)
        self.goto(x_side, y_side)
        self.refresh()

    def refresh(self):
        x_side = random.randint(-280, 280)
        y_side = random.randint(-280, 280)

        self.goto(x_side, y_side)
