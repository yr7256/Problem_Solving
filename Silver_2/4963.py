from collections import deque
dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]


def bfs(n, m):
    field[n][m] = 0
    queue = deque()
    queue.append([n, m])
    while queue:
        x0, y0 = queue.popleft()
        for i in range(8):
            x1 = x0+dx[i]
            y1 = y0+dy[i]
            if 0 <= x1 < h and 0 <= y1 < w and field[x1][y1] == 1:
                field[x1][y1] = 0
                queue.append([x1, y1])


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    field = [list(map(int, input().split())) for i in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if field[i][j] == 1:
                bfs(i, j)
                count += 1
    print(count)
