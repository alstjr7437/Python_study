#1 ~ 10 sum 짝수
sum = 0
for i in range(2, 11, 2) :
    sum += i
    print(i, "+", sum - i, "=", sum)
'''
for i in range(1, 11) :
    if (i%2==0) :
        sum += i
        print(i, "+", sum - i, "=", sum)
'''