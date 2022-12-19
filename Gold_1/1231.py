C, D, M = map(int, input().split())
stocks = [list(map(int, input().split())) for _ in range(C)]
dp = [[0 for _ in range(500001)] for _ in range(D+1)]
for i in range(1, D+1):
    dp[1][M] = M
    for j in range(1, 500001):
        for k in range(C):
            if stocks[k][i] <= j and (stocks[k][i]-stocks[k][i-1]):
                dp[i][j] = max(dp[i][j], dp[i][j-stocks[k][i]]+(stocks[k][i]-stocks[k][i-1]))
