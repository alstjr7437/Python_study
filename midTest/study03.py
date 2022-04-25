aa = []             #리스트 선언
aa.append(0)
aa.append(0)
aa.append(0)
print(len(aa))      #print len을 안하면 출력X
a = [10,20,30,40]
print("a[-1]은 %d, a[-2]는 %d"%(a[-1], a[-2]))
print(a[0:3])
print(a[0:4:2])
print("a[2:]",a[2:])
print(a[:2])
print(a[::2])
print(a[::-2])
print(a * 3, a + aa)

b = [10,20,30]
b[1:2] = [200,201]
print(b)
b[1:4] = [200,201]
print(b)
b[1] = [20,30]
print(b)
del(b[1])
print(b)
b = []
print(b)
b = None
print(b)

