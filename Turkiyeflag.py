from turtle import *

speed(0)

bgcolor("black")

penup()
goto(-300, 170)

pencolor("red")
fillcolor("red")

pendown()
begin_fill()

for i in range(2):
    forward(600)
    right(90)
    forward(350)
    right(90)

end_fill()

#circle

penup()
goto(-130, -120)

pencolor("white")
fillcolor("white")
begin_fill()

circle(120)

end_fill()

#redcircle

penup()
goto(-80, -100)

pencolor("red")
fillcolor("red")
begin_fill()

circle(100)

end_fill()

#star

penup()
goto(-15, -25)
pendown()

pencolor("white")
fillcolor("white")

begin_fill()

for i in range(5):
    forward(40)
    left(144)
    forward(40)
    right(72)

end_fill()

mainloop()