from turtle import *
import random

bgcolor("black")
speed(0)
def stars():
    fillcolor("white")
    pencolor("white")
    begin_fill()
    for i in range (5):
        forward(10)
        right(144)
    end_fill()
#main function

for i in range(150):
    x = random.randint(-600, 600)
    y = random.randint(-350, 350)
    penup()
    goto(x, y)
    pendown()
    stars() 

penup()
goto(140, 150)
pendown()

pencolor("white")
fillcolor("white")
begin_fill()
circle(100)
end_fill()

penup()
goto(170, 150)
pendown()

pencolor("black")
fillcolor("black")
begin_fill()
circle(100)
end_fill()

hideturtle()

mainloop()