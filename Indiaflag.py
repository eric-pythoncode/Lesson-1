from turtle import *

speed(0)

bgcolor("black")

pencolor("orange")
fillcolor("orange")
begin_fill()

for s in range (2):
    forward(350)
    left(90)
    forward(70)
    left(90)

end_fill()

#red rectangle

pencolor("white")
fillcolor("white")
begin_fill()

for s in range (2):
    forward(350)
    right(90)
    forward(70)
    right(90)

end_fill()

#yellow rectangle

right(90)
forward(70)
left(90)

pencolor("green")
fillcolor("green")
begin_fill()

for s in range (2):
    forward(350)
    right(90)
    forward(70)
    right(90)

end_fill()

#circle

penup()
goto(175, -70)

pencolor("blue")
fillcolor("blue")

begin_fill()

circle(35)

end_fill()

#white circle

goto(175, -60)

pencolor("white")
fillcolor("white")

begin_fill()

circle(25)

end_fill()

#blue circle

penup()

goto(175, -50)

pendown()

pencolor("blue")
fillcolor("blue")

begin_fill()

circle(15)

end_fill()

mainloop()