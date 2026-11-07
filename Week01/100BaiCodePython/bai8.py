from math import* 

a, b, c = map(int, input().split())
cv = a + b + c
p = cv / 2
s = sqrt(p * (p - a) * (p - b) * (p - c))
r = a * b * c / (4 * s)
print(f'{r:.3f}')