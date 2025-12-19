import turtle
import random
import time
dealy=0.1
hs=0
sc=0
bodies=[]


s1=turtle.Screen()
s1.title("Snake Game")
s1.bgcolor("white")
s1.setup(width=700,height=700)
s1.tracer(0)

h1=turtle.Turtle()
h1.shape("circle")
h1.fillcolor("red")
h1.penup()
h1.goto(0,0)
h1.direction="stop"

f1=turtle.Turtle()
f1.shape("square")
f1.fillcolor("green")
f1.penup()
f1.goto(200,200)
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
        h1.sety(h1.ycor()+20)
    if h1.direction=="down":
        h1.sety(h1.ycor()-20)
    if h1.direction=="left":
        h1.setx(h1.xcor()-20)
    if h1.direction=="right":
        h1.setx(h1.xcor()+20)
        
s1.listen()
s1.onkey(moveup,"Up")
s1.onkey(movedown,"Down")
s1.onkey(moveleft,"Left")
s1.onkey(moveright,"Right")

while True:
    s1.update()

    if h1.xcor()>290:  h1.setx(-290)
    if h1.xcor()<-290: h1.setx(290)
    if h1.ycor()>290:  h1.sety(-290)
    if h1.ycor()<-290: h1.sety(290)
        
    
    if h1.distance(f1)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        f1.goto(x,y)

        b1=turtle.Turtle()
        b1.speed(0)
        b1.penup()
        b1.shape("square")
        b1.color("yellow")
        bodies.append(b1)

        sc+=10
        if sc>hs:
            hs=sc
        s2.clear()
        s2.write(f"score:{sc}|hight score:{hs}",font=("Arial",14,"normal"))
        dealy-=0.001
    for i in range(len(bodies)-1,0,-1):
        x=bodies[i-1].xcor()
        y=bodies[i-1].ycor()
        bodies[i].goto(x,y)
    if len(bodies)>0:
        x=h1.xcor()
        y=h1.ycor()
        bodies[0].goto(x,y)
    move()
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
            s2.write(f"score:{sc}|highest score:{hs}",font=("Arial",14,"normal"))
            msg=turtle.Turtle()
            msg.clear()
            msg.goto(0,0)
            msg.write("Game Over",align="center",font=("Arial",14,"normal"))
            time.sleep(1)
            msg.clear()
    time.sleep(dealy)
s.mainloop()