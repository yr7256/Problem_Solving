from collections import deque
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
x0, y0 = 0, 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'I':
            x0, y0 = i, j
queue = deque([[x0, y0]])
visited[x0][y0] = 1
ans = 0
while queue:
    x, y = queue.popleft()
    for i in range(4):
        x1 = x+dx[i]
        y1 = y+dy[i]
        if 0 <= x1 < N and 0 <= y1 < M and not visited[x1][y1] and arr[x1][y1] != 'X':
            queue.append([x1, y1])
            visited[x1][y1] = 1
            if arr[x1][y1] == 'P':
                ans += 1
print(ans if ans else 'TT')
