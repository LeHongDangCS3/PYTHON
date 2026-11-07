from math import* 

n = int(input())
a = list(map(int, input().split()))
x = max(a)
print(x, a.index(x))