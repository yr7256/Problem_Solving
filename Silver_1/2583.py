'''
bfs 돌거니까 deque 필요함!
4방향 탐색하면서 최대 어느정도까지 갈 수 있을까 count 해본다.
이미 찍은 지점이면 탐색 x
'''
from collections import deque


def bfs(x, y):
    count = 1
    queue = deque([[x, y]])
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            x1 = x+dx[i]
            y1 = y+dy[i]
            if 0 <= x1 < N and 0 <= y1 < M:
                if not arr[x1][y1] and not visited[x1][y1]:
                    queue.append([x1, y1])
                    visited[x1][y1] = 1
                    count += 1
    return count


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
M, N, K = map(int, input().split())
arr = [[0]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]
for _ in range(K):
    x0, y0, x1, y1 = map(int, input().split())
    for i in range(x0, x1):
        for j in range(y0, y1):
            arr[i][j] = 1
check = []
for i in range(N):
    for j in range(M):
        if not arr[i][j] and not visited[i][j]:
            check.append(bfs(i, j))
check.sort()
print(len(check))
print(*check)
