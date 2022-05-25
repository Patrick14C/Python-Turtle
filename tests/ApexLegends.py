from turtle import *

title("Apex Legends")
screensize(600, 600)
speed(15)
hideturtle()

def logo(): #Logo
    pu()
    goto(-45, -100)
    left(180)
    pd()
    
    fillcolor("black")
    begin_fill()
    
    forward(50)
    right(120)
    forward(150)
    right(120)
    forward(150)
    right(120)
    forward(50)
    left(150)
    forward(100)
    left(80)
    forward(80)
    left(70)
    forward(321)
    left(120)
    forward(321)
    left(70)
    forward(80)
    left(81)
    forward(99)
    
    end_fill()
    
logo()

done()