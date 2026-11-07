from math import* 

m, n = map(int, input().split())
tong = 0
cnt = 0
for i in range(m, n + 1):
    if i % 2 == 0:
        tong += i
    if i % 3 == 0 or i % 5 == 0:
       cnt += 1
print(cnt, tong)
