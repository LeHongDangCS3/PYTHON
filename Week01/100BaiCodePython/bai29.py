from math import* 

def ngto(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
if ngto(n):
    print("Yes")
else:
    print("No")