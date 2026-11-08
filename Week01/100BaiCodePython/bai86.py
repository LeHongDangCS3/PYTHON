from math import*

def chuvi(a, b, c):
    cv = a + b + c
    print(f'{cv:.1f}', end=' ')

def dientich(a, b, c):
    p = (a + b + c) / 2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    print(f'{s:.3f}', end=' ')

a, b, c = map(int, input().split())
chuvi(a, b, c)
dientich(a, b, c)