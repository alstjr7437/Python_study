import operator

d = {'apple':200,'ce':200,'ba':150}
# print(d.keys())

t = sorted(d.items(), key = operator.itemgetter(0), reverse = True)

print(t)
#for i in d.keys() :
#    print(f"{i} > {d[i]}")