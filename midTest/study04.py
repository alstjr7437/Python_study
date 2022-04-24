#리스트
#리스트는 다른 언어와 다르게 다른 데이터형도 묶을 수 있는것

list1 = []
list2 = []
value = 0
for i in range(0,4):
    for j in range(0,5):
        list1.append(value)
        value += 3
    list2.append(list1)
    list1 = []

for i in range(0,4):
    for j in range(0,5):
        print("%3d" %list2[i][j], end = "")
    print()