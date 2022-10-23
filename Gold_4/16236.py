import sys
from collections import deque
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited = [[0]*N for i in range(N)]
    visited[x][y] = 1
    time = 0
    shark = 2
    eat = 0
    ate = False
    answer = 0
    while queue:
        queue = deque(sorted(queue))
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if field[x][y] != 0 and field[x][y] < shark:
                field[x][y] = 0
                eat += 1
                if eat == shark:
                    shark += 1
                    eat = 0
                queue = deque()
                visited = [[0]*N for i in range(N)]
                visited[x][y] = 1
                ate = True
                answer = time
            for i in range(4):
                x1 = x+dx[i]
                y1 = y+dy[i]
                if 0 <= x1 < N and 0 <= y1 < N and visited[x1][y1] == 0:
                    if field[x1][y1] <= shark:
                        queue.append([x1, y1])
                        visited[x1][y1] = 1
            if ate == True:
                ate = False
                break
        time += 1
    return answer


N = int(input())
field = [list(map(int, input().split())) for i in range(N)]
for i in range(N):
    for j in range(N):
        if field[i][j] == 9:
            x0, y0 = i, j
            field[i][j] = 0
print(bfs(x0, y0))
