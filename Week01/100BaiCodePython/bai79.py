from math import* 

s = input()

a = {}
s = s.lower()
for x in s:
    if x not in a:
        a[x] = 1
    else:
        a[x] += 1
m = max(a.values()) 
for key, value in a.items():
    if value == m:
        print(f'{key}:{value}')
        break