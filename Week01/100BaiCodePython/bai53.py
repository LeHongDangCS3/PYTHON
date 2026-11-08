from math import* 

def ngto(n):
    if n < 2: 
        return False
    for i in range (2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True 

a = list(map(int, input().split()))
b = []
for i in a:
    if ngto(i):
        b.append(i)
if len(b) == 0:
    print('-')
else:
    print(max(b))