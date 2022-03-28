import random
import turtle as t
t.shape("turtle")
t.screensize(100,100)
t.speed(50)
x,y = 0,0

while 1 :
        r = random.random()
        g = random.random()
        b = random.random()
        width = random.randrange(0,100)
        angle = random.randrange(0,360)
        w = random.randrange(0,20)

        t.pensize(w)
        t.pencolor(r,g,b)
        t.left(angle)
        t.forward(width)
        x = t.xcor()
        y = t.ycor()
        print(f"x = {x} y = {y}")
        if(-200 < x < 200 or -200 < y < 200) :
            pass
        else :
            t.penup()
            t.goto(0,0)
            t.pendown()
