from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.color("Black")
        self.penup()
        self.setheading(90)
        self.setposition(STARTING_POSITION)
        self.i = 0
    def player_move(self):
        self.forward(MOVE_DISTANCE)


    def finish(self):
        self.goto(STARTING_POSITION)

    def level_counter(self):
        self.i+=self.i