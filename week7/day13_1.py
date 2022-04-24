aa = [10,20,30]
print(aa[::2])
print(aa[1:3])
print(aa[:2])

bb = [[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]]

print(bb)
print(bb[1])
print(bb[1][2])

cc = [[1,2,3],
      [4,5,6],
      [7,8,9]]
for i,j in range(3):
    for j in range(3):
        print(cc[i][j], end=' ');
    print(" ")