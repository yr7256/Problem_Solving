import sys
input = sys.stdin.readline


def half(n, k):
    if k == 1:
        return n
    if k % 2 == 0:
        return (half(n, k//2)**2) % p
    else:
        return (half(n, k//2)**2*n) % p


M = int(input())
p = 1000000007
fac = [1]*4000001
for i in range(2, 4000001):
    fac[i] = (fac[i-1]*i) % p
for i in range(M):
    N, K = map(int, input().split())
    print(fac[N]*half(fac[K]*fac[N-K], p-2) % p)
