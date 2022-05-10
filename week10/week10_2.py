import random

a = []
num = 0;

print("로또 번호")

while 1 :
    num = random.randrange(1,46)
    if a.count(num) == 0 :
        a.append(num)

    if len(a) > 7 :
        break;

a.sort()
for i in range(0,6):
    print(a[i], end = "  ")