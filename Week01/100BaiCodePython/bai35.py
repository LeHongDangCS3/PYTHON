from math import*

def ngto(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

m, n = map(int, input().split())
cnt = 0
tong = 0
for i in range(m, n + 1):
    if ngto(i):
        cnt += 1
        tong += i
c = tong / cnt
print(f"{c:.2f}")