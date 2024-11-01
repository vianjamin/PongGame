from turtle import Turtle

OPP_SIDE = 280
OPP_STARTING_POSITIONS = [(OPP_SIDE, -20), (OPP_SIDE, 0), (OPP_SIDE, 20)]


class Opponent:

    def __init__(self):
        self.create_opponent_paddle()

    def create_opponent_paddle(self):
        paddle = Turtle("square")
        paddle.color("white")
        paddle.shape("square")
        paddle.shapesize(stretch_len=1, stretch_wid=4)
        paddle.penup()
        paddle.goto(x=-350, y=0)
