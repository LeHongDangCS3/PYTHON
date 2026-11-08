from math import*

a = {}

while True:
    x = input()
    if x == '':
        break

    x = int(x)
    a[x] = 1
print(len(a))