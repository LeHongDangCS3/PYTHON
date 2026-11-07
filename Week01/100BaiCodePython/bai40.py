from math import*

def scp(n):
    x = int(sqrt(n))
    return x * x == n

n = int(input())
cnt = 0
dem = 0
while True and dem < n:
    if scp(cnt):
        print(cnt, end=" ")
        dem += 1
    cnt += 1
