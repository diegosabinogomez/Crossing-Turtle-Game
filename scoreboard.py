from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 35, 'normal')
class Scoreboard(Turtle):
    """Class to model the scoreboard and game over display"""
    def __init__(self):
        super().__init__()
        self.points = 0
        self.color("black")
        self.penup()
        # self.write("test", move=False, align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"{self.points}", move=False, align=ALIGNMENT, font=FONT)

    def increase_points(self):
        self.points += 1

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)