from turtle import *

bgcolor("black")
pencolor("white")
fillcolor("white")
begin_fill()

penup()
goto(-200,-100)
pendown()

for i in range(2):
    forward(350)
    left(90)
    forward(200)
    left(90)

end_fill()

penup()
goto(-25, -60)
pendown()
fillcolor("red")
pencolor("red")
begin_fill()

circle(60)

end_fill()

penup()
goto(-140, 120)
pendown()
write("Japan", font=("TImes New Roman", 75))
hideturtle()
mainloop()