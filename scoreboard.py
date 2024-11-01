from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.enemy_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.player_score} : {self.enemy_score}", align=ALIGN, font=FONT)

    def increase_player_score(self):
        self.player_score += 1
        self.clear()
        self.update_scoreboard()

    def increase_enemy_score(self):
        self.enemy_score += 1
        self.clear()
        self.update_scoreboard()

    def end(self):
        self.goto(0,0)
        if self.player_score > self.enemy_score:
            self.write("Game over! You win!", align=ALIGN, font=FONT)
        else:
            self.write("Game over! Opponent wins", align=ALIGN, font=FONT)
