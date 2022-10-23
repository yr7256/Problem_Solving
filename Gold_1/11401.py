N, K = map(int, input().split())
p = 1000000007
dp = [1 for i in range(N+1)]
for i in range(2, N+1):
    dp[i] = dp[i-1]*i % p


def square(a, b):
    if b == 0:
        return 1
    if b % 2:
        return square(a, b//2)**2*a % p
    else:
        return square(a, b//2)**2 % p


print(dp[N]*square(dp[K]*dp[N-K] % p, p-2) % p)
