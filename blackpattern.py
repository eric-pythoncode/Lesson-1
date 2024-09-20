from turtle import *

speed(0)
pensize(6)
pencolor("navy")

circle(100)

forward(13)
left(90)
forward(4)
right(90)
for i in range(24):
    circle(1)
    left(15)
    penup()
    forward(25)
    pendown()

penup()

goto(0, 100)

pendown()

for i in range(24):
    pencolor("navy")
    forward(100)
    backward(100)
    left(360/24)

penup()

left(6)
forward(95)

pendown()
left(60)

hideturtle()

mainloop()