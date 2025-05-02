import random
from turtle import Turtle
MOVE_DISTANCE = 10
X0_POSITIONS = []
for i in range(-300, 301):
    X0_POSITIONS.append(i)
colors = ["blue", "red", "yellow", "orange", "black", "brown", "grey"]

class Traffic(Turtle):
    """This class represents the 'traffic' and all its attributes and methods. The cars are inside the list obstacles"""
    def __init__(self):
        super().__init__()
        self.obstacles = []
        self.create_obstacles()


    def create_obstacles(self):
        """The 'traffic' is a list with the individual cars, being a car of the class Turtle()"""
        for pos_y in range(-280, 300, 20):
            car = Turtle(shape="square")
            car.penup()
            car.color(random.choice(colors))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.goto(random.choice(X0_POSITIONS),pos_y)
            self.obstacles.append(car)

    def move(self):
        """Move each car in the list obstacles"""
        for car in self.obstacles:
            car.backward(MOVE_DISTANCE)

    def reappear(self):
        """For when the cars reach the rightmost part of the screen"""
        for auto in self.obstacles:
            if auto.xcor() < -320:
                auto.goto(300, auto.ycor())


