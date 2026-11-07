from math import*  

n = int(input())
cnt = 0
for i in range(1, int(sqrt(n)) + 1):
    if i * i == n:
        cnt += 1
    elif n % i == 0:
        cnt += 2
print(cnt)
