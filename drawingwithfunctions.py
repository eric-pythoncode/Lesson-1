from turtle import *

speed(0)

bgcolor("lightblue")

def square(size, color):
    fillcolor(color)
    pencolor(color)
    begin_fill()
    for i in range(4):
        forward(size)
        right(90)
    end_fill()

def triangle(size, color):
    fillcolor(color)
    pencolor(color)
    begin_fill()
    for i in range(3):
        forward(size)
        left(120)
    end_fill()

def rectangle(size, color):
    fillcolor(color)
    pencolor(color)
    begin_fill()
    for i in range(2):
        forward(size / 2)
        right(90)
        forward(size)
        right(90)
    end_fill()

#main program

penup()
goto(-100, 0)
pendown()

square(200, "brown")
triangle(200, "yellow")

#right window
penup()
goto(-70, -30)
pendown()

square(50, "white")

#left window
penup()
goto(20, -30)
pendown()

square(50, "white")

#door
penup()
goto(-25, -100)
pendown()

rectangle(100, "green")

#treebark
penup()
goto(200, -120)
pendown()

rectangle(80, "brown")

#treeleaf
penup()
goto(175, -120)
pendown()

triangle(90, "green")

#treeleaf2
penup()
goto(175, -150)
pendown()

triangle(90, "green")

#treeleaf3
penup()
goto(175, -90)
pendown()

triangle(90, "green")

#sun

penup()
goto(-225, 150)
pendown()

fillcolor("orange")
pencolor("red")
begin_fill()
circle(60)
end_fill()

hideturtle()

mainloop()