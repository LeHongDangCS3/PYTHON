from math import* 

a, b, c = map(float, input().split())
if a + b > c and a + c > b and b + c > a:
    print('Day la 3 canh cua mot tam giac')
    cv = a + b + c 
    p = cv / 2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    print(f'{cv:.2f} {s:.1f}')
else:
    print('Day khong phai la 3 canh cua mot tam giac')