from math import factorial
N = int(input())
fac_inv = str(factorial(N))[::-1]
for i in fac_inv:
    if i == '0':
        continue
    else:
        print(i)
        break
