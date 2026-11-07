from math import* 

n = int(input())

if n >= 11 or n == 1:
    print('Mua Dong')
elif n >= 8:
    print('Mua Thu')
elif n >= 5:
    print('Mua Ha')
else:
    print('Mua Xuan')