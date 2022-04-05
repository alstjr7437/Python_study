import turtle as t

t.pensize(4)
t.shape("turtle")

t.color("blue")
t.bgcolor("yellow")
t.fillcolor("red")

##ㅗ모양
t.begin_fill()
t.left(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(300)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.end_fill()

##바깥 원 모양
t.penup()
t.goto(50, -300)
t.pendown()

t.begin_fill()
t.circle(100)
t.end_fill()

##안쪽 원 모양
t.fillcolor("yellow")
t.penup()
t.goto(50, -250)
t.pendown()

t.begin_fill()
t.circle(50)
t.end_fill()

t.done()