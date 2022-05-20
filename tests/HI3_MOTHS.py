from turtle import *

colors = ["red", "white"]
a = -60; b = 120

title("MOTHS")
setup(800, 600, 0, 0)
screensize(600, 400)
hideturtle()
speed(15)
pensize(5)

def square(l): #Funcion cuadrado
    forward(l)
    left(90)
    forward(l)
    left(90)
    forward(l)
    left(90)
    forward(l)

for i in range(2):
    fillcolor(colors[i])
    begin_fill()
    pu()
    goto(0, a)
    pd()
    circle(b)
    end_fill()
    a += 30; b+= -30

pu()
goto(0, 10)
forward(200)
pd()
left(90)
circle(200, 180)
circle(200, 180)

done()