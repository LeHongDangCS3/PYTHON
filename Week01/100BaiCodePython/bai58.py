from math import*

a = {}

while True:
    x = input()
    if x == '':
        break
    if x not in a:
        a[x] = 1
    else:
        a[x] += 1

for key, value in a.items():
    print(key, value)
    print()