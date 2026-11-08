from math import* 

a = list(map(int, input().split()))
if len(a) <= 1:
    print('-')
else:
    a = sorted(a)
    a = list(reversed(a))
    vtri = a.count(a[0])
    if vtri == 1:
        print(a[1])
    else:
        print(a[vtri])