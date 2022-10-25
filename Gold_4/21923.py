import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
up = [[-INF]*M for _ in range(N)]
down = [[-INF]*M for _ in range(N)]
up[N-1][0] = arr[N-1][0]
down[N-1][M-1] = arr[N-1][M-1]
for i in range(N-1, -1, -1):
    for j in range(M):
        if i == N-1 and j == 0:
            continue
        if i < N-1:
            up[i][j] = max(up[i][j], up[i+1][j])
        if j > 0:
            up[i][j] = max(up[i][j], up[i][j-1])
        up[i][j] += arr[i][j]
for i in range(N-1, -1, -1):
    for j in range(M-1, -1, -1):
        if i == N-1 and j == M-1:
            continue
        if i < N-1:
            down[i][j] = max(down[i][j], down[i+1][j])
        if j < M-1:
            down[i][j] = max(down[i][j], down[i][j+1])
        down[i][j] += arr[i][j]
ans = -INF
for i in range(N):
    for j in range(M):
        ans = max(ans, up[i][j]+down[i][j])
print(ans)
