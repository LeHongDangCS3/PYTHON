from math import* 

t, m = map(int, input().split())
g = gcd(t, m)
t /= g
m /= g
print(f"{int(t)}/{int(m)}")
