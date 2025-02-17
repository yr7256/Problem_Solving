from collections import deque


def move(x, y, d):
    count = 0
    while arr[x+dx[d]][y+dy[d]] != '#' and arr[x][y] != 'O':
        x += dx[d]
        y += dy[d]
        count += 1
    return x, y, count


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = []
rx, ry, bx, by = 0, 0, 0, 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            rx, ry = i, j
        elif arr[i][j] == 'B':
            bx, by = i, j
queue = deque([[rx, ry, bx, by, 1]])
visited.append([rx, ry, bx, by])
while queue:
    rx0, ry0, bx0, by0, ans = queue.popleft()
    if ans > 10:
        print(-1)
        exit()
    for i in range(4):
        rx1, ry1, rcnt = move(rx0, ry0, i)
        bx1, by1, bcnt = move(bx0, by0, i)
        if arr[bx1][by1] == 'O':
            continue
        if arr[rx1][ry1] == 'O':
            print(ans)
            exit()
        if rx1 == bx1 and ry1 == by1:
            if rcnt > bcnt:
                rx1 -= dx[i]
                ry1 -= dy[i]
            if rcnt < bcnt:
                bx1 -= dx[i]
                by1 -= dy[i]
        if [rx1, ry1, bx1, by1] not in visited:
            visited.append([rx1, ry1, bx1, by1])
            queue.append([rx1, ry1, bx1, by1, ans+1])
print(-1)
