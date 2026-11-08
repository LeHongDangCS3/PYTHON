from math import* 

def scp(n):
   x = int(sqrt(n))
   return x * x == n

a = list(map(int, input().split()))
cnt = 0
tong = 0
for x in a:
   if x < 0: continue
   if scp(x):
      cnt += 1
      tong += x
if cnt == 0:
   print('-')
else:
   c = tong / cnt
   print(f'{c:.1f}')
