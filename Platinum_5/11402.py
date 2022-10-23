from math import comb
N, K, M = map(int, input().split())
x = 1
while N or K:
    x *= comb(N % M, K % M)
    x %= M
    if x == 0:
        break
    N //= M
    K //= M
print(x)
