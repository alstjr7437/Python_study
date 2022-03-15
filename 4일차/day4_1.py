import turtle as t
t.shape("turtle")
t.fillcolor("blue")
t.pencolor("white")

t.screensize(500, 500, bg="yellow")
t.setup(600, 600)

t.penup()
t.goto(-250, 250)
t.pendown()

t.pensize(10)

t.begin_fill()
for i in range(4):
    t.forward(100)
    t.right(90)
t.end_fill()
t.color("black")

t.done()