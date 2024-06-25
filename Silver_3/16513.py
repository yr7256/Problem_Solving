from math import gcd
from decimal import Decimal
x, y = input().split()
num = len(x[x.find('.')+1:])
a = int(Decimal(x)*10**num)-int(Decimal(x)*10**(num-int(y)))
b = 10**num-10**(num-int(y))
c = gcd(a, b)
print(a//c, b//c, sep='/')
