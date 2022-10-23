from collections import deque
import copy
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
field = [list(map(int, input().split())) for i in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    queue = deque()
    field_2 = copy.deepcopy(field)
    for i in range(N):
        for j in range(M):
            if field[i][j] == 2:
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            x1 = x+dx[i]
            y1 = y+dy[i]
            if 0 <= x1 < N and 0 <= y1 < M and field_2[x1][y1] == 0:
                field_2[x1][y1] = 2
                queue.append((x1, y1))
    global answer
    count = 0
    for i in field_2:
        for j in i:
            if j == 0:
                count += 1
    answer = max(answer, count)


def wall(x):
    if x == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if field[i][j] == 0:
                field[i][j] = 1
                wall(x+1)
                field[i][j] = 0


answer = 0
wall(0)
print(answer)
