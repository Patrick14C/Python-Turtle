from turtle import *

colors = ["red", "white"]
a = -60; b = 120

title("MOTHS")
setup(800, 600, 0, 0)
screensize(600, 400)
hideturtle()
speed(15)
pensize(5)

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
left(145)
pd()

def semi_c():
    for i in range(90):
        left(10)
        forward(30)
        
semi_c()

done()