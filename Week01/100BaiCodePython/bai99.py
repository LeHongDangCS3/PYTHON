from math import* 

def scp(n):
    if n > 0:
        x = int(sqrt(n))
        return x * x == n

a = list(map(int, input().split()))
cnt = 0
tong = 0
for i in a:
    if scp(i):
         cnt += 1
         tong += i
if cnt == 0:
    print('-')
else:
    c = tong / cnt 
    print(f'{c:.1f}')
    