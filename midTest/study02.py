fruit = ['사과', '배', '딸기']
if '사과' in fruit :
    print("사과 있어요!")
for i in range(0, 10, 2):       #시작, 끝, 옮기는 범위(0부터 9까지 2칸씩)
    print(i)
for i in range(10, 0, -1):      #10부터 1까지 -1씩
    print("hello world!", i)
for i in range(7, -1, -1):      #7부터 0까지 -1씩
    print(i)
i = 0
while i < 3:            #while문  변수 < 끝값
    print("%d번 반복"%i)
    i = i+1
while True :        #계속 반복
    print("hello")
    break           #break로 나가기