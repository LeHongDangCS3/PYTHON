from math import* 

s = input()
cnt = 0
for x in s:
    if(x.isupper()):
        cnt += 1
print(cnt)