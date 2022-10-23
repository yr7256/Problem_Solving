import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
cheese = [list(map(int, input().split())) for i in range(N)]
count = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque([])
for i in range(N):
    for j in range(M):
        if cheese[i][j] == 1:
            queue.append([i, j])


def bfs():
    queue = deque()
    queue.append([0, 0])
    visited = [[False]*M for i in range(N)]
    visited[0][0] = True
    while queue:
        x0, y0 = queue.popleft()
        for i in range(4):
            x1 = x0+dx[i]
            y1 = y0+dy[i]
            if 0 <= x1 < N and 0 <= y1 < M:
                if visited[x1][y1] == False:
                    if cheese[x1][y1] >= 1:
                        cheese[x1][y1] += 1
                    else:
                        visited[x1][y1] = True
                        queue.append([x1, y1])


while True:
    bfs()
    flag = False
    for i in range(N):
        for j in range(M):
            if cheese[i][j] >= 3:
                cheese[i][j] = 0
                flag = True
            elif cheese[i][j] > 0:
                cheese[i][j] = 1
    if flag:
        count += 1
    else:
        break
print(count)
