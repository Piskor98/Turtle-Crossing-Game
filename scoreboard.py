from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.goto(-250,250)
        self.write(f"Level: {self.score}", font = FONT)


    def increase_level(self):
        self.score+=1
        self.clear()
        self.write(f"Level: {self.score}", font=FONT)

    def losing(self):
        self.clear()
        self.write(f"You lose at stage: {self.score}", font = FONT)