from math import* 

m, y = map(int, input().split())

if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
    if m == 2:
        print(29)
    elif m in [1, 3, 5, 7, 8, 10, 12]:
        print(31)
    else:
        print(30)
else:
    if m == 2:
        print(28)
    elif m in [1, 3, 5, 7, 8, 10, 12]:
        print(31)
    else:
        print(30)