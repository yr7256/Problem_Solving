import sys
input = sys.stdin.readline
T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = [[x, y]]
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            x1 = x+dx[i]
            y1 = y+dy[i]
            if 0 <= x1 < N and 0 <= y1 < M and field[x1][y1] == 1:
                field[x1][y1] = 0
                queue.append([x1, y1])


for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0]*(M) for i in range(N)]
    count = 0
    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                bfs(i, j)
                field[i][j] = 0
                count += 1
    print(count)
