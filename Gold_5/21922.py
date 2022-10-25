from collections import deque
import sys

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
queue = deque([])
for i in range(N):
    for j in range(M):
        if arr[i][j] == 9:
            visited[i][j] = 1
            queue.append((i, j))
while queue:
    x0, y0 = queue.popleft()
    for i in range(4):
        dex, dey = dx[i], dy[i]
        x1, y1 = x0+dex, y0+dey
        while 0 <= x1 < N and 0 <= y1 < M:
            visited[x1][y1] = 1
            if arr[x1][y1] == 9:
                break
            if arr[x1][y1] == 3:
                dex, dey = -dey, -dex
            if arr[x1][y1] == 4:
                dex, dey = dey, dex
            if (arr[x1][y1] == 1 and dex == 0) or (arr[x1][y1] == 2 and dey == 0):
                break
            x1 += dex
            y1 += dey
ans = 0
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            ans += 1
print(ans)