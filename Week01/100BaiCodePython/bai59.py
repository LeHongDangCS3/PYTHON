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
m = max(a.values())
for key, value in a.items():
    if value == m:
        print(key, value)
        break