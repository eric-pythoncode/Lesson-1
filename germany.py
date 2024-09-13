from turtle import *


pencolor("black")
fillcolor("black")
begin_fill()

for s in range (2):
    forward(350)
    left(90)
    forward(70)
    left(90)

end_fill()

#red rectangle

pencolor("red")
fillcolor("red")
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

pencolor("#FFCC00")
fillcolor("#FFCC00")
begin_fill()

for s in range (2):
    forward(350)
    right(90)
    forward(70)
    right(90)

end_fill()

mainloop()