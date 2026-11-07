from math import*

n = int(input())
a = list(map(int, input().split()))
b = []
c = []
cnt1 = 0
cnt2 = 0
for i in a:
    if i > 0:
        cnt1 += 1
        b.append(i)
    else:
        cnt2 += 1
        c.append(i)
print (cnt1, cnt2)
print(*b)
print(*c)