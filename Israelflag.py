from turtle import *

speed(0)

penup()
goto(-200,100)
pendown()

bgcolor("black")

#white rectangle

pencolor("white")
fillcolor("white")
begin_fill()

for s in range (2):
    forward(350)
    right(90)
    forward(35)
    right(90)

end_fill()

#blue rectangle

right(90)
forward(35)
left(90)

pencolor("blue")
fillcolor("blue")
begin_fill()

for s in range (2):
    forward(350)
    right(90)
    forward(35)
    right(90)

end_fill()

#white rectangle

right(90)
forward(35)
left(90)

pencolor("white")
fillcolor("white")
begin_fill()

for s in range (2):
    forward(350)
    right(90)
    forward(140)
    right(90)

end_fill()

#blue rectangle

right(90)
forward(140)
left(90)
pencolor("blue")
fillcolor("blue")
begin_fill()

for s in range (2):
    forward(350)
    right(90)
    forward(35)
    right(90)

end_fill()

#white rectangle

right(90)
forward(35)
left(90)

pencolor("white")
fillcolor("white")
begin_fill()

for s in range (2):
    forward(350)
    right(90)
    forward(35)
    right(90)

end_fill()

#star

penup()
goto(-70,0)
pendown()

pencolor("blue")
pensize(5)

for i in range(3):
    forward(100)
    right(120)

#other star

penup()
goto(-70,-70)
pendown()

pencolor("blue")
pensize(5)

for i in range(3):
    forward(100)
    left(120)


mainloop()