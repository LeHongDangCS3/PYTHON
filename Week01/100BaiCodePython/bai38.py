from math import*

def ngto(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
cnt = 0
dem = 0
while True and dem < n:
    if ngto(cnt):
        print(cnt, end=" ")
        dem += 1
    cnt += 1
