import turtle
import random

##함수 부분
# 왼쪽 마우스버튼 클릭하여 도장찍기
def screenLeftClick(x, y):
    global r,g,b
    r = random.random()
    g = random.random()
    b = random.random()
    
#크기는 2부터 10
    tSize = random.randrange(2,10)
#각도는 0부터 360도 
    tAngle = random.randrange(0, 360)
#크기 색상 각도
    turtle.shapesize(tSize)
    turtle.color(r,g,b)
    turtle.right(tAngle)
#거북이 도장 찍기
    turtle.stamp()

#거북이 이동 
def screenRightClick(x,y):
    turtle.penup()
    turtle.goto(x,y)

##변수 부분
#변수 초기값
r,g,b = 0.0,0.0,0.0

##메인 부분
turtle.title("거북이 도장 찍기")
turtle.shape("turtle")

#함수 호출
turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenRightClick,3)

turtle.done()

