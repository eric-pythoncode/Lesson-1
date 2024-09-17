from turtle import *

speed(0)

penup()
goto(-200, 100)
pendown()

#red rectangle

pencolor("#f0cb11")
fillcolor("#f0cb11")
begin_fill()

for s in range (2):
    forward(350)
    left(90)
    forward(70)
    left(90)

end_fill()

#green rectangle

pencolor("green")
fillcolor("green")
begin_fill()

for s in range (2):
    forward(350)
    right(90)
    forward(70)
    right(90)

end_fill()

#red rectangle

right(90)
forward(70)
left(90)

pencolor("red")
fillcolor("red")
begin_fill()

for s in range (2):
    forward(350)
    right(90)
    forward(70)
    right(90)

end_fill()

#star

penup()
goto(-15, 45)
pendown()

pencolor("white")
fillcolor("white")

begin_fill()

for i in range(5):
    forward(45)
    left(144)
    forward(45)
    right(72)

end_fill()


mainloop()