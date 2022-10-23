import sys
from collections import deque
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N, M = map(int, input().split())
field = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1  # x값, y값, 벽뚫 안뚫
queue = deque([[0, 0, 0]])
while queue:
    x, y, destroy = queue.popleft()
    if x == N-1 and y == M-1:
        print(visited[x][y][destroy])
        break
    for i in range(4):
        x1 = x+dx[i]
        y1 = y+dy[i]
        if 0 <= x1 < N and 0 <= y1 < M:
            if field[x1][y1] == 0 and visited[x1][y1][destroy] == 0:
                visited[x1][y1][destroy] = visited[x][y][destroy]+1
                queue.append([x1, y1, destroy])
            elif field[x1][y1] == 1 and destroy == 0:
                visited[x1][y1][1] = visited[x][y][0]+1
                queue.append([x1, y1, 1])
else:
    print(-1)
