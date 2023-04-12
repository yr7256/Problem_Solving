dp = [[1]*1001 for _ in range(1001)]
for i in range(2, 1001):
    for j in range(2, 1001):
        dp[i][j] = (dp[i-1][j-1]+dp[i-1][j]+dp[i][j-1])%1000000007
n, m = map(int, input().split())
print(dp[n][m])