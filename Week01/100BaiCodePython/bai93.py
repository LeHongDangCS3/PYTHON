from math import* 

def nn(a, b):
    return min(a, b)

a, b, c = map(int, input().split())
print(nn(nn(a, b), c))