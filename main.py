"""Main script. We have to implement an instance of the class Turtle to model the screen. The screen tracer(0) freezes
updating the screem. It refreshes once the interpreter reaches screen.update(). screen.exitonclick() holds the screen ON.
The speed of the game is controlled by time.sleep(TIME_INCREASE)"""

from turtle import Screen
from turtle_crossing import TurtleCrossing
from traffic import Traffic
from scoreboard import Scoreboard
import time

TIME_INCREASE = 0.3

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Project")
screen.tracer(0)

traffic = Traffic()
traffic.hideturtle()
turtle_crossing = TurtleCrossing()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(turtle_crossing.up, "Up")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(TIME_INCREASE*turtle_crossing.v_coef)
    traffic.move()
    traffic.reappear()

    if turtle_crossing.ycor() > 290:
        turtle_crossing.restart()
        scoreboard.increase_points()
        scoreboard.update_scoreboard()

    # Detect collision with a car
    for auto in traffic.obstacles:
        if turtle_crossing.distance(auto) < 19:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()