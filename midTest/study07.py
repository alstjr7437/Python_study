import operator

aa, bb = {},{}

aa = {'bage':3, 'age': 1, 'center':2}
bb = sorted(aa.items(), key=operator.itemgetter(0), reverse = True)

print(bb)

data = {"철수":98, "영희":80, "순이":100,"돌이":70}
sum = 0
for i in data.keys() :
    print('%s %4d' %(i,data[i]))
    sum += data[i]
avg = sum / len(data)
print('평균 %4d' %(avg))

set1 = {1,2,3,4,5}      #딕셔너리 키만 모으는 특수 형태 (중복은 안됨)
set2 = {4,5,6,7}
print(set1 & set2)      #교집합
print(set1 | set2)      #합집합
print(set1 - set2)      #차집합
print(set1 ^ set2)      #대칭집합

numL = [num for num in range(1,6)]          #리스트 = [수식 for 항목 in range() if 조건식]
print(numL)
numL2 = [num for num in range(1,21) if num % 3 == 0]
print(numL2)

a = ['a','b','c','d','e']
b = [1,2,3]
for s in zip(a,b):
    print(s)
    print(list(s))
tup = list(zip(a,b))
dic = dict(zip(a,b))
print(tup)
print(dic)