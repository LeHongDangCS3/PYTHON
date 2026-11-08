from math import* 

def maxmin(a):
    b = max(a)
    c = min(a)
    return b, c


n = int(input())
a = list(map(int, input().split()))
b, c = maxmin(a)
print(b, a.index(b))
print(c, a.index(c))