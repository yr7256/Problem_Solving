import sys
input = sys.stdin.readline
INF = sys.maxsize
N = int(input())
ans = INF
RGB = [list(map(int, input().split())) for _ in range(N)]
for j in range(3):
    dp = [[INF]*3 for _ in range(N)]
    dp[0][j] = RGB[0][j]
    for i in range(1, N):
        dp[i][0] = RGB[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = RGB[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = RGB[i][2] + min(dp[i-1][0], dp[i-1][1])
    for k in range(3):
        if k != j:
            ans = min(ans, dp[N-1][k])
print(ans)