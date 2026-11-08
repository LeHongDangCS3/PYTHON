from math import* 

def cong(a):
   return sum(a)


n = int(input())
a = list(map(int, input().split()))
m = len(a) 
c = cong(a) / m
print(f'{c:.1f}')
