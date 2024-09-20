from turtle import *

pensize(5)

for i in range(8):
    pencolor("red")
    forward(55)
    backward(55)
    left(360/24)
    pencolor("navy")
    forward(75)
    backward(75)
    left(360/24)
    pencolor("green")
    forward(95)
    backward(95)
    left(360/24)
mainloop()