N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
dp = [0]*(N+1)
for i in range(N-1, -1, -1):
    if i + table[i][0] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(table[i][1] + dp[i + table[i][0]], dp[i+1])
print(dp[0])
