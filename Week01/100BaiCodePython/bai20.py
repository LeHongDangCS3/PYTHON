from math import* 

n = int(input())
k5 = n // 5000
k2 = (n % 5000) // 2000
k1 = (n % 5000 % 2000) // 1000
print(k5, k2, k1)