import turtle
import random       #색깔 랜덤으로 하기 위해

##함수 선언 부분##
#왼쪽 클릭으로 그림 그리기 색깔 바꾸기
def screenLeftClick(x, y):
    global r, g, b
    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.goto(x, y)
    r = random.random()
    g = random.random()
    b = random.random()
#오른쪽 클릭으로 옮기기
def screenRightClick(x, y):
    turtle.penup()
    turtle.goto(x, y)
#중간 클릭으로 거북이 크기수정
def screenMidClick(x, y):
    global r, g, b
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)

##변수 선언 부분##
pSize, tSize = 10, 0
r, g, b = 0.0, 0.0, 0.0

##메인 코드 부분##
turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

#함수 호출 부분
turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()

