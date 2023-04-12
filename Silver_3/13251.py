from math import comb
M = int(input())
stones = list(map(int, input().split()))
K = int(input())
S = sum(stones)
a = comb(S, K)
b = 0
for i in stones:
    b += comb(i, K)
print(b/a)
