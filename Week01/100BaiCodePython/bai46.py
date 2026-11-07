from math import* 

n, x = map(int, input().split())
a = list(map(int, input().split()))

if x in a:
    print('Yes')
    print(a.index(x))
else:
    print('No')