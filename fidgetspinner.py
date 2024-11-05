from turtle import *
import turtle

s = Screen()
s.title("Fidget Spinner")
s.bgcolor("light blue")


t1 = turtle.Turtle()
t1.hideturtle()
t1.penup()
t1.goto(-130,160)
t1.pendown()
t1.write("Fidget Spinner!!" , font = ("times" , 20 , "bold"))

state = {'turn': 0}

def spinner():

    clear()

    angle = state['turn']/10

    right(angle)

    forward(100)

    dot(120, "pink")

    back(100)

    right(120)

    forward(100)

    dot(120, 'darkseagreen')

    back(100)

    right(120)

    forward(100)

    dot(120, 'gold')

    back(100)

    right(120)

    update()


def animate():

    if state['turn']>0:

        state['turn']-=1


    spinner()

    ontimer(animate, 20)


def flick():

    state['turn']+=10

setup(420, 420, 370, 0)

hideturtle()

tracer(False)

width(20)

onkey(flick, 'space')

listen()

animate()

done()

