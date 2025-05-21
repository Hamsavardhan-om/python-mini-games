import turtle

def player1():
    redCar.forward(5)
def player2():
    blueCar.forward(5)

road = turtle.Screen()
road.bgpic("Race.gif")
road.addshape("Red Car.gif")
road.addshape("Blue Car.gif")

redCar = turtle.Turtle()
redCar.setheading(90)
redCar.shape("Red Car.gif")
redCar.penup()
redCar.goto(-100,-240)

blueCar = turtle.Turtle()
blueCar.setheading(90)
blueCar.shape("Blue Car.gif")
blueCar.penup()
blueCar.goto(100,-240)

turtle.onkeypress(player1,"Up")
turtle.onkeypress(player2,"w")
turtle.listen()

while True:
    road.update()
    if redCar.pos() >= (-100,200):
       redCar.hideturtle()
       blueCar.hideturtle()
       road.bgpic("Red car Wins.gif")
    if blueCar.pos() >= (100,200):
       redCar.hideturtle()
       blueCar.hideturtle()
       road.bgpic("Blue car Wins.gif")

turtle.done()