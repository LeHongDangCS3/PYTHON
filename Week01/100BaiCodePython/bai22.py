from math import* 

n = int(input())
s = 0

if n > 200:
    s += 50 * 600 + 50 * 800 + 100 * 1100 + (n - 200) * 1500
elif n > 100:
    s += 50 * 600 + 50 * 800 + (n - 100) * 1100
elif n > 50:
    s += 50 * 600 + (n - 50) * 800
else:
    s += n * 600
print(s)