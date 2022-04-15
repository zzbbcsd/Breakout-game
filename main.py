from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from block import Block
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("white")
screen.setup(width=900, height=800)
screen.title("Welcome to Breakout Game")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()

title = Turtle()
title.penup()
title.hideturtle()
title.goto(-140,350)
title.write("Use <- and -> keys to move", align="center", font=("Courier", 20, "normal"))
# create blocks
x_cor = -390

blocks = []

while x_cor <= 400:
    block_r = Block((x_cor,300),"red")
    blocks.append(block_r)

    block_o = Block((x_cor,255), "orange")
    blocks.append(block_o)

    block_g = Block((x_cor,210), "green")
    blocks.append(block_g)

    block_b = Block((x_cor,165),"blue")
    blocks.append(block_b)

    print(x_cor)
    x_cor += 85


screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

game_is_on = True

while game_is_on and len(blocks)>=0:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 390:
        ball.bounce_y()
    if ball.xcor() > 430 or ball.xcor()<-440:
        ball.bounce_x()
    # detect collision with paddle
    if ball.ycor() <- 360 and ball.distance(paddle) < 50 :
        ball.bounce_y()

    # detect collision with block
    for block in blocks:
        if block.distance(ball) < 50:
            ball.bounce_y_accelerate()
            block.hideturtle()
            blocks.remove(block)
            scoreboard.score_up()


    # end game if the ball hits the floor
    if ball.ycor()<-380:
        game_is_on=False
        scoreboard.game_over()

screen.exitonclick()
