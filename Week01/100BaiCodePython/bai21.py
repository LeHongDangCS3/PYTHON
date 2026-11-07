from math import* 

n = int(input())
s = 0
if n >= 31:
    s += 1 * 12000 + (30 - 1) * 10000 + (n - 30) * 9000
elif n >= 2:
    s += 1 * 12000 + (n - 1) * 10000
else:
    s += 1 * 12000
print(s) 