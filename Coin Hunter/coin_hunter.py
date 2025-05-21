import turtle
import random

score = 0

def left():
    hunter.shape("left_transparent.gif")
    hunter.backward(10)

def right():
    hunter.shape("right_transparent.gif")
    hunter.forward(10)

def move():
    y = coin.ycor()
    coin.sety(y-2.5)

def move_2():
    y = coin.ycor()
    coin.sety(y-4.5)

def move_3():
    y = coin.ycor()
    coin.sety(y-6)

def move_4():
    y = coin.ycor()
    coin.sety(y-8)

sea = turtle.Screen()
sea.bgpic("sea.gif")
sea.addshape("left_transparent.gif")
sea.addshape("right_transparent.gif")
sea.addshape("coin.gif")

hunter = turtle.Turtle()
hunter.shape("left_transparent.gif")
hunter.penup()
hunter.goto(0,-150)

coin = turtle.Turtle()
coin.shape("coin.gif")
coin.speed(1000)
coin.penup()
coin.goto(-280,280)

scoreBoard = turtle.Turtle()
scoreBoard.speed(1000)
scoreBoard.penup()
scoreBoard.goto(-100,240)
scoreBoard.write("Score: " + str(score),font=("Courier",27,"bold"))
scoreBoard.hideturtle()

turtle.onkeypress(left,"a")
turtle.onkeypress(right,"d")
turtle.listen()

while True:
    sea.update()
    if score < 10:
        move()
    elif score >= 10 and score < 20:
        move_2()
    elif score > 20 and score < 30:
        move_3()
    else:
        move_4()
    if coin.ycor() < -300:
        x = random.randint(-280,280)
        coin.goto(x,280)
    if hunter.distance(coin) < 50:
        score = score + 1
        scoreBoard.clear()
        scoreBoard.write("Score: {}".format(score),font=("Courier",27,"bold"))
        x = random.randint(-280,280)
        coin.goto(x,280)

turtle.done()