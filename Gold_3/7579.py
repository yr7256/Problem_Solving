import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
byte = [0]+list(map(int, input().split()))
inactivate = [0]+list(map(int, input().split()))
dp = [[0]*(sum(inactivate)+1) for _ in range(N+1)]
ans = INF
for i in range(1, N+1):
    for j in range(1, sum(inactivate)+1):
        if inactivate[i] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-inactivate[i]]+byte[i])
        if dp[i][j] >= M:
            ans = min(ans, j)
# print(dp)
print(ans)