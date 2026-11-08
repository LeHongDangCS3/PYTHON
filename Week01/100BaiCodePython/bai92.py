from math import* 

a, b, c = map(int, input().split())
n1 = a + b + c 
n2 = a / b + c
n3 = a / (b + c)
print(f'n1 {n2:.2f} {n3:.3f}')