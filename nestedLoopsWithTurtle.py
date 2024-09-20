from turtle import *
speed(0)
color = ["red","green","blue","yellow","orange","magenta","black","white"]
pensize(2)
for i in range(15):
    for j in color:
        pencolor(j)
        circle(150)
        left(3)
mainloop()