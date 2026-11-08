from math import* 

def ngto(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

a = list(map(int, input().split()))
cnt = 0
for x in a:
    if ngto(x):
         cnt += 1
print(cnt)