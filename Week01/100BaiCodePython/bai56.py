from math import*

a = {}

while True:
    x = input()
    if x == '':
        break

    x = int(x)
    a[x] = 1

if len(a) < 3:
    print(-1)
else:
    b = sorted(a.keys())
    print(b[2])