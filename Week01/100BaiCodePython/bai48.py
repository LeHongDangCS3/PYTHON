from math import* 

n = int(input())
a = list(map(int, input().split()))
tong = 0
for i in a:
    if i % 5 == 0:
        tong += i
        print(i, end=" ")
if tong == 0:
    print('-')
else:
    print()
    print(tong)
