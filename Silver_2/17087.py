from math import gcd
N, S = map(int, input().split())
bro = list(map(int, input().split()))
A = []
for i in bro:
    A.append(abs(i-S))
result = min(A)
for i in range(len(A)):
    result = gcd(result, A[i])
print(result)
