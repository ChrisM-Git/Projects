from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time
screen = Screen()

screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("PONG")
#paddle will not show in screen with tracer until you create a while loop
screen.tracer(0)

screen.listen()
rpaddle = Paddle((350, 0))
lpaddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.onkey(rpaddle.R_Up, "Up")
screen.onkey(rpaddle.R_Down,"Down")
screen.onkey(lpaddle.L_Up, "w")
screen.onkey(lpaddle.L_Down,"s")



gameon = True

while gameon:
    screen.update()
    # sloq the ball movement)
    time.sleep(ball.movespeed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.xcor() > 380:
        ball.resetball()
        scoreboard.rpoint()
        ball.movespeed *= 0.9


    if ball.xcor() < -380:
        ball.resetball()
        scoreboard.lpoint()
        ball.movespeed *= 0.9

    #check if ball hits right ppaddle

    if ball.distance(rpaddle) < 30 and ball.xcor() > 310 or ball.distance(lpaddle) < 30 and ball.xcor() < -310:
        ball.paddlebounce()

    #right paddle miss, 380 is the x distance + paddle width


screen.exitonclick()