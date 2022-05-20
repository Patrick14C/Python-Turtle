from turtle import *

title("Instagram")
setup(500, 500)
pencolor("black")
speed(20)
pensize(15)
hideturtle()

pu()
goto(-70, -70)
pd()

def cuadrado():
    forward(140)
    circle(60, 90)
    forward(140)
    circle(60, 90)
    forward(140)
    circle(60, 90)
    forward(140)
    circle(60, 90)

def centro():
    circle(70)
    
def circulo():
    fillcolor("black")
    begin_fill()
    circle(10)
    end_fill()

cuadrado()
pu()
goto(0,-15)
pd()
centro()
pu()
home()
goto(75, 130)
pd()
circulo()

done()