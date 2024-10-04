from turtle import *
import random

penup()
goto(-150, 150)
for i in range(1, 16):
    write(i, align="center")
    right(90)
    forward(10)
    pendown()
    for j in range(10):
        penup()
        forward(10)
        pendown()
        forward(10)
    penup()
    backward(210)
    left(90)
    forward(20)

racer1 = Turtle()
racer1.color("red")
racer1.shape("turtle")
racer1.penup()
racer1.pensize(5)
racer1.goto(-170, 100)
racer1.pendown()

racer2 = Turtle()
racer2.color("green")
racer2.shape("turtle")
racer2.penup()
racer2.pensize(5)
racer2.goto(-170, 60)
racer2.pendown()

racer3 = Turtle()
racer3.color("blue")
racer3.shape("turtle")
racer3.penup()
racer3.pensize(5)
racer3.goto(-170, 20)
racer3.pendown()

racer4 = Turtle()
racer4.color("yellow")
racer4.shape("turtle")
racer4.penup()
racer4.pensize(5)
racer4.goto(-170, -20)
racer4.pendown()

for i in range(50):
    racer1.forward(random.randint(1, 10))
    racer2.forward(random.randint(1, 10))
    racer3.forward(random.randint(1, 10))
    racer4.forward(random.randint(1, 10))
mainloop()