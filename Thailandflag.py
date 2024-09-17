from turtle import *

bgcolor("black")

penup()
goto(-150, 100)
pendown()
#red rectangle
pencolor("red")
fillcolor("red")
begin_fill()

for s in range (2):
    forward(350)
    right(90)
    forward(45)
    right(90)

end_fill()

#white rectangle

pencolor("white")
fillcolor("white")
begin_fill()

penup()
right(90)
forward(45)
left(90)
pendown()
for s in range (2):
    forward(350)
    right(90)
    forward(45)
    right(90)

end_fill()

#blue rectangle

pencolor("navy")
fillcolor("navy")
begin_fill()

penup()
right(90)
forward(45)
left(90)
pendown()
for s in range (2):
    forward(350)
    right(90)
    forward(75)
    right(90)

end_fill()

#white rectangle

pencolor("white")
fillcolor("white")
begin_fill()

penup()
right(90)
forward(75)
left(90)
pendown()
for s in range (2):
    forward(350)
    right(90)
    forward(45)
    right(90)

end_fill()

#red rectangle

penup()
right(90)
forward(45)
left(90)
pendown()

pencolor("red")
fillcolor("red")
begin_fill()

for s in range (2):
    forward(350)
    right(90)
    forward(45)
    right(90)

end_fill()

hideturtle()


mainloop()