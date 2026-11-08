from math import* 

def ngto(n):
    if n < 2: 
        return False
    for i in range (2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True 

a = list(map(int, input().split()))
tong = 0
for i in a:
    if ngto(i):
        tong += i
        print(i, end = ' ')
if(tong == 0):
    print('-')
else:
    print()
    print(tong)
