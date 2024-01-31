from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
x0, y0 = 0, 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            x0, y0 = i, j
queue = deque([[x0, y0]])
arr[x0][y0] = 0
visited[x0][y0] = 1
while queue:
    x, y = queue.popleft()
    for i in range(4):
        x1 = x+dx[i]
        y1 = y+dy[i]
        if 0 <= x1 < n and 0 <= y1 < m and not visited[x1][y1] and arr[x1][y1] == 1:
            visited[x1][y1] = 1
            arr[x1][y1] = arr[x][y] + 1
            queue.append([x1, y1])
for i in range(n):
    for j in range(m):
        if not visited[i][j] and arr[i][j]:
            arr[i][j] = -1
for i in range(n):
    print(*arr[i])
