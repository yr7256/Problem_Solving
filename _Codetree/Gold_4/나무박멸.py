from copy import deepcopy
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ddx = [1, 1, -1, -1]
ddy = [1, -1, 1, -1]
n, m, k, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
ans = 0
for year in range(m):
    next_arr = deepcopy(arr)
    trees = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                trees.append([i, j])
                cnt = 0
                spread = 0
                for d in range(4):
                    x1 = i+dx[d]
                    y1 = j+dy[d]
                    if 0 <= x1 < n and 0 <= y1 < n:
                        if arr[x1][y1] > 0:
                            cnt += 1
                        if not arr[x1][y1] and not visited[x1][y1]:
                            spread += 1
                next_arr[i][j] += cnt
                if not spread:
                    continue
                grow = next_arr[i][j]//spread
                for dd in range(4):
                    x2 = i+dx[dd]
                    y2 = j+dy[dd]
                    if 0 <= x2 < n and 0 <= y2 < n and not arr[x2][y2] and not visited[x2][y2]:
                        next_arr[x2][y2] += grow
                        if not [x2, y2] in trees:
                            trees.append([x2, y2])
    arr = deepcopy(next_arr)
    kill = 0
    kx, ky = 0, 0
    trees.sort()
    if not trees:
        continue
    for x, y in trees:
        if arr[x][y]:
            temp = arr[x][y]
            for d in range(4):
                x1 = x+ddx[d]
                y1 = y+ddy[d]
                for _ in range(k):
                    if 0 <= x1 < n and 0 <= y1 < n and arr[x1][y1] > 0:
                        temp += arr[x1][y1]
                        x1 += ddx[d]
                        y1 += ddy[d]
            if temp > kill:
                kill = temp
                kx, ky = x, y
    for i in range(n):
        for j in range(n):
            if visited[i][j] > 0:
                visited[i][j] -= 1
    ans += arr[kx][ky]
    arr[kx][ky] = 0
    visited[kx][ky] = c
    for d in range(4):
        x1 = kx+ddx[d]
        y1 = ky+ddy[d]
        for _ in range(k):
            if 0 <= x1 < n and 0 <= y1 < n:
                visited[x1][y1] = c
                if arr[x1][y1] <= 0:
                    break
                ans += arr[x1][y1]
                arr[x1][y1] = 0
                x1 += ddx[d]
                y1 += ddy[d]
print(ans)