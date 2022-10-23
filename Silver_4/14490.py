from math import gcd
n, m = (map(int, input().split(':')))
print(n//gcd(n, m), m//gcd(n, m), sep=':')
