import turtle

def Up():
    rocket.setheading(90)
    rocket.forward(20)
    rocket.setheading(0)

def Down():
    rocket.setheading(270)
    rocket.forward(20)
    rocket.setheading(0)

def Left():
    rocket.setheading(180)
    rocket.forward(20)
    rocket.setheading(0)

def Right():
    rocket.forward(20)

space = turtle.Screen()
space.bgpic("space_game_intro.gif")

def func():
    space.bgpic("maze.gif")

while space.bgpic() == "space_game_intro.gif":
    space.update()
    turtle.onkeypress(func,"space")
    turtle.listen()

rocket = turtle.Turtle()
rocket.speed(1000)
spaceman = turtle.Turtle()
spaceman.speed(1000)

space.addshape("rocket.gif")
rocket.shape("rocket.gif")
space.addshape("astronaut.gif")
spaceman.shape("astronaut.gif")

rocket.penup()
rocket.goto(180,-250)
spaceman.penup()
spaceman.goto(-103,255)

turtle.onkey(Up,"w")
turtle.onkey(Down,"s")
turtle.onkey(Left,"a")
turtle.onkey(Right,"d")
turtle.listen()

while True:
    space.update()
    if(rocket.distance(spaceman) < 10):
        rocket.hideturtle()
        spaceman.hideturtle()
        space.bgpic("end_screen.gif")

turtle.done()