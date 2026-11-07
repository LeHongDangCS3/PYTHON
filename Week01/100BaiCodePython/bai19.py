from math import* 

n = input()
s = 0
for i in range(len(n)):
    s += int(n[i])
print(s % 10)
if s % 10 == 9:
    print('may man')
else:
    print('chua may man')