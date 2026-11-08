from math import *

def rutgon(a, b):
    g = gcd(a, b)
    a //= g
    b //= g

    if b < 0:
        a = -a
        b = -b

    return a, b

def cong(a, b, c, d):
    return rutgon(a * d + b * c, b * d)

def tru(a, b, c, d):
    return rutgon(a * d - b * c, b * d)

def nhan(a, b, c, d):
    return rutgon(a * c, b * d)

def chia(a, b, c, d):
    return rutgon(a * d, b * c)

def inra(a, b):
    if abs(a) >= b:
        nguyen = a // b
        tu = abs(a) % b
        if tu == 0:
            print(nguyen)
        else:
            print(f'{nguyen},{tu}/{b}')
    else:
        print(f'{a}/{b}')


a, b = map(int, input().split())
c, d = map(int, input().split())

inra(*cong(a, b, c, d))
inra(*tru(a, b, c, d))
inra(*nhan(a, b, c, d))
inra(*chia(a, b, c, d))