from math import* 

s =input()
a = []
for x in s:
    if x not in a:
        a.append(x)
print(len(a))