import turtle
#import random
import numpy as np
import time
dealy=0.1
hs=0
sc=0
bodies=[]


s1=turtle.Turtle()
s1.tilt("Snake Game")
s1.bgcolor("black")
s1.setup(width=700,hight=700)

h1=turtle.Turtle()
h1.shape("circle")
h1.shape()
h1.fillcolor("green")
h1.penup()
h1.goto(0,0)
h1.direction="stop"

f1=turtle.Turtle()
f1.shape("circle")
f1.shape()
f1.fillcolor("green")
f1.penup()
f1.ht()
f1.goto(100,100)
f1.st()
f1.direction="stop"

s2=turtle.Turtle()
s2.ht()
s2.penup()
s2.goto(-250,250)
s2.write("sceor:0|highest sceor:0")

def moveup():
    if h1.direction!="down":
        h1.direction="up"
def movedown():
    if h1.direction!="up":
        h1.direction="down"
def moveleft():
    if h1.direction!="right":
        h1.direction="left"
def moveright():
    if h1.direction!="left":
        h1.direction="right"
def move():
    if h1.direction=="up":
        y=h1.ycor()
        h1.sety(y+20)
    if h1.direction!="down":
        y=h1.ycor()
        h1.setx(y-20)
    if h1.direction=="left":
        x=h1.xcor()
        h1.setx(x+20)
    if h1.direction!="right":
        x=h1.xcor()
        h1.setx(x-20)
s1.listen()
s1.onclick(moveup,"up")
s1.onclick(movedown,"down")
s1.onclick(moveleft,"left")
s1.onclick(moveright,"right")
while True:
    s1.update()
    if h1.xcor()>290:
        h1.setx(-290)
    if h1.xcor()<-290:
        h1.setx(290)
    if h1.ycor()>290:
        h1.sety(-290)
    if h1.ycor()<-290:
        h1.sety(290)
    
    if h1.distance(f1)<20:
        x=np.random.randint(-290,290)
        y=np.random.randint(-290,290)
        f1.goto(x,y)

        b1=turtle.Turtle()
        b1.speed(0)
        b1.penup()
        b1.shape("square")
        b1.color("yellow")
        bodies.append()

        sc=sc+5
        if sc>hs:
            hs=sc
        s2.color()
        s2.write(f"score:{sc}|hight score:{hs}",font=("Arial",14,"normal"))
        dealy=dealy-0.001
    for b in bodies:
        if b.distance(h1)<20:
            time.sleep(1)
            h1.goto(0,0)
            h1.direction="stop"
            for b in bodies:
                b.ht()
            bodies.clear()
            sc=0
            s2.clear()
            s2.write(f"score:0|highest score:{hs}",font=("Arial",14,"normal"))
            msg=turtle.Turtle()
            msg.clear()
            msg.goto(0,0)
            msg.write("Game Over",align="center",font=("Arial",14,"normal"))
            time.sleep()
            msg.clear()
    time.sleep(dealy)
s.mainloop()