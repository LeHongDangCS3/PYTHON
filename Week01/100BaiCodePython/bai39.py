from math import* 

def scp(n):
    x = int(sqrt(n))
    return x * x == n 

n = int(input())
if scp(n):
    print("Yes")
else:
    print("No")