from turtle import *
import random
wn=Screen()
global score
score=0
t=Turtle()
t.speed(50)
t.pencolor('red')
t.pensize(3)
t1=Turtle()
t1.penup()
t1.pencolor('maroon')
td=Turtle()
td.pencolor('blue')
td.penup()
td.hideturtle()
ts=Turtle()
ts.hideturtle()
ts.penup()
ts.goto(100,200)
ts.write('Score : '+str(score),font=("Verdana",15, "normal"))
def forw():
    t1.setheading(90)
def back():
    t1.setheading(270)
def rit():
    t1.setheading(0)
def lit():
    t1.setheading(180)
def d():
    td.goto(random.randint(-195,195),random.randint(-195,195))
    global p1
    p1=td.pos()
    td.pendown()
    td.dot(8)
    td.penup()
def d_c(q):
    if p1[0]-2<=q[0]<=p1[0]+2  and  p1[1]-2<=q[1]<=p1[1]+2:
        for i in range(3):
            td.undo()
        return True
listen()
onkey(forw,'Up')
onkey(back,'Down')
onkey(rit,'Right')
onkey(lit,'Left')
t.penup()
t.setpos(200,-200)
t.pendown()
t.lt(90)
for i in range(4):
    t.fd(400)
    t.lt(90)
t.hideturtle()
d()
con=True
go=Turtle()
go.hideturtle()
go.penup()
go.bk(50)
while con:
    t1.fd(1)
    p=t1.pos()
    if d_c(p):
        score+=1
        ts.undo()
        ts.write('Score : '+str(score),font=("Verdana",15, "normal"))
        d()
    if ((-200.00>=p[0])or(p[0]>=200.00))or((-200.00>=p[1])or(p[1]>=200.00)):
        con=False
        go.write('Game Over',font=("Verdana",20, "normal"))
wn.exitonclick()
