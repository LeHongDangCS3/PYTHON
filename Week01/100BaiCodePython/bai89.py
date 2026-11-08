from math import*

def giaithua(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s

n = int(input())
tong = 0

for i in range(n):
    a, b = map(int, input().split())
    tong += giaithua(a) // (giaithua(b) * giaithua(a - b))

print(tong)