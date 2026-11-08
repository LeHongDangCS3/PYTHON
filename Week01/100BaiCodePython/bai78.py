from math import* 

s = input()

a = {}
s = s.lower()
for x in s:
    if x not in a:
        a[x] = 1
    else:
        a[x] += 1

for key, value in a.items():
    print(f'{key}:{value}', end = ' ')