import sys
input = sys.stdin.readline
C, D, M = map(int, input().split())
stocks = [list(map(int, input().split())) for _ in range(C)]
dp = [[i for i in range(500001)] for _ in range(D)]
for i in range(1, D):
    for k in range(C):
        for j in range(stocks[k][i-1], M+1):
            dp[i][j] = max(dp[i][j], dp[i][j-stocks[k][i-1]]+stocks[k][i])
    M = dp[i][M]
    for l in range(M+1):
        dp[i][l] = l
print(M)
