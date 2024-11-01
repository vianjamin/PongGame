
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


from line import Line

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
Line()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, key="Up")
screen.onkey(r_paddle.down, key="Down")
screen.onkey(l_paddle.up, key="w")
screen.onkey(l_paddle.down, key="s")

game_is_on = True
while game_is_on:

    time.sleep(ball.move_speeds)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() == 400:
        score.increase_enemy_score()
        ball.reset_position()

    elif ball.xcor() == -400:
        score.increase_player_score()
        ball.reset_position()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if score.player_score == 3 or score.enemy_score == 3:
        game_is_on = False
        score.end()


screen.exitonclick()



