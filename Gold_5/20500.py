dp = [[0]*3 for i in range(1516)]
dp[1][1] = 1
for i in range(2, 1516):
    dp[i][0] = dp[i-1][1]+dp[i-1][2]
    dp[i][1] = dp[i-1][0]+dp[i-1][2]
    dp[i][2] = dp[i-1][0]+dp[i-1][1]
N = int(input())
print(dp[N][0] % 1000000007)
