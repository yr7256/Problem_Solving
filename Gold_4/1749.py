import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
arr = [[0]*(M+1)]+[[0]+list(map(int, input().split())) for _ in range(N)]
dp = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        arr[i][j] += arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1]
ans = -INF
for i in range(1, N+1):
    for j in range(1, M+1):
        for k in range(i):
            for l in range(j):
                ans = max(ans, arr[i][j]-arr[k][j]-arr[i][l]+arr[k][l])
print(ans)
