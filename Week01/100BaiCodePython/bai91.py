from math import* 

def hcn(d, r):
    print('*' * d)
    x = 0
    while x < r - 2:
        print('*', end = '')
        for i in range (1, d - 1):
            print(' ', end = '')
        print('*', end = '')
        print()
        x += 1
    print('*' * d)
d, r = map(int, input().split())
hcn(d, r)
