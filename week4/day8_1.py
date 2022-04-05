import turtle as t
import random

t.speed(100)
width = 500
height = 500
t.shape("turtle")
t.setup(550, 550)
t.screensize(500,500)
t.penup()
t.goto(0,-height/2)
t.pendown()

for i in range(0,250) :
    ran = random.randrange(0,6)
    if ran == 0 :
        t.pencolor("red")
    elif ran == 1 :
        t.pencolor("orange")
    elif ran == 2 :
        t.pencolor("yellow")
    elif ran == 3 :
        t.pencolor("green")
    elif ran == 4 :
        t.pencolor("blue")
    elif ran == 5 :
        t.pencolor("purple")
    t.circle(i)
t.done()

