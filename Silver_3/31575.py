from collections import deque
dx = [0, 1]
dy = [1, 0]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
visited = [[0]*N for _ in range(M)]
queue = deque([[0, 0]])
visited[0][0] = 1
while queue:
    x, y = queue.popleft()
    for i in range(2):
        x1 = x+dx[i]
        y1 = y+dy[i]
        if 0 <= x1 < M and 0 <= y1 < N and not visited[x1][y1] and arr[x1][y1]:
            visited[x1][y1] = 1
            queue.append([x1, y1])
print('Yes' if visited[M-1][N-1] else 'No')
