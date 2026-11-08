from math import* 

def mu(n, k):
    return n ** k


k, x = map(int, input().split())
tong = 0
for i in range (k):
    a, n = map(int, input().split())
    tong += a * mu(x, n)
print(tong)