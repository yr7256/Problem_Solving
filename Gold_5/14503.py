def robot(x, y, d):
    global block
    if field[x][y] == 0:
        field[x][y] = 2
        block += 1
    for i in range(4):
        d1 = (d+3) % 4
        x1 = x+dx[d1]
        y1 = y+dy[d1]
        if 0 <= x1 < N and 0 <= y1 < M and field[x1][y1] == 0:
            robot(x1, y1, d1)
            return
        d = d1
    d1 = (d+2) % 4
    x1 = x+dx[d1]
    y1 = y+dy[d1]
    if field[x1][y1] == 1:
        return
    robot(x1, y1, d)


N, M = map(int, input().split())
r, c, d = map(int, input().split())
field = [list(map(int, input().split())) for i in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
block = 0
robot(r, c, d)
print(block)
