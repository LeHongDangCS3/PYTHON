from math import *

def ucln(a, b):
    return gcd(a, b)

a, b = map(int, input().split())

g = ucln(a, b)
a //= g
b //= g

print(f'{a}/{b}')