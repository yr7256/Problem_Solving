N = int(input())
dp = [[0]*10 for i in range(N)]
dp[0] = [1]*10
for i in range(1, N):
    for j in range(10):
        dp[i][j] = dp[i][j-1]+dp[i-1][j]
print(sum(dp[N-1]) % 10007)
