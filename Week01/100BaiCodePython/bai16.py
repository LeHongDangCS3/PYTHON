from math import* 

a, b = map(float, input().split())

tbcn = (a + b * 2) / 3

print(f'{tbcn:.1f}')
if tbcn >= 8:
    print('Gioi')
elif tbcn >= 6.5:
    print('Kha')
elif tbcn >= 5:
    print('Trung binh')
elif tbcn >= 3.5:
    print('Yeu')
else:
    print('Kem')
