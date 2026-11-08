from math import*

def tbc(a):
    tong = 0
    cnt = 0
    for x in a:
        if x % 2 == 0:
            tong += x
            cnt += 1
    c = tong / cnt
    print(f'{c:.2f}')

n = int(input())
a = list(map(int, input().split()))
tbc(a)
