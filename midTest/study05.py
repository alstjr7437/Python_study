#튜플
#튜플은 리스트와 같지만 값 수정이 안됨 ()이용

a = (10,20,30)      #튜플 > 리스트와 다르게 값 수정X
b = 10,20,30        #튜플은 괄호 생략 가능

print(a[1])
print(b)
#a[1] = 10      #값은 수정 불가로 오류 발생
del(a)          #전체 삭제 가능

print(b[1:3])   #리스트와 같이 접근 가능
c = ('A', 'B')
print(b + c)    #마찬가지로 리스트 같이 연산 가능
print(b * 2)

tt = ((1,2,3),
      (4,5,6),
      (7,8,9))
for i in range(0,3) :
    for j in range(0,3):
        print("%3d"%tt[i][j], end="")
    print()

mTuple = 10,20,30
mList = list(mTuple)
mList.append(40)            #튜플은 수정이 안되므로 list로 바꿧다가 다시 튜플 바꾸기
mTuple = tuple(mList)
print(mTuple)