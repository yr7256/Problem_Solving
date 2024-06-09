N, M = map(int, input().split())
num = 1000000007
dp = [1]*(N+1)
if N >= M:
    dp[M] = 2
for i in range(M+1, N+1):
    dp[i] = (dp[i-1]+dp[i-M]) % num
print(dp[N] % num if N >= M else 1)
