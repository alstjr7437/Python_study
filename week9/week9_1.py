aa = [1,2,3,4,5]

print(aa[3])
print(aa[0:4])

bb = "Happy"
print(bb.count("H"))
print(bb[0:3])
print(bb[:3])

ss = "파이썬짱!"

for i in range(0, len(ss)):
    print(ss[i] + '$', end = "")

print()
for i in range(len(ss)-1, -1, -1):
    print(ss[i], end="")

import Turtle