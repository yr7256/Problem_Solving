from math import gcd
A, B = map(int, input().split())
C, D = map(int, input().split())
E = A*D+B*C
F = B*D
G = gcd(E, F)
print(E//G, F//G)
