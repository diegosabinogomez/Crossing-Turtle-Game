from turtle import Turtle
MOVE_DISTANCE = 10

class TurtleCrossing(Turtle):
    """Class to model the crossing turtle. """
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.goto(0,-280)
        self.setheading(90)
        self.v_coef = 1

    def up(self):
        self.forward(MOVE_DISTANCE)

    def restart(self):
        self.goto(0, -280)
        self.v_coef *= 0.9



