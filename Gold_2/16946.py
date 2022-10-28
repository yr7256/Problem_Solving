import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
wall_visited = [[0]*M for _ in range(N)]
ans = [[0]*M for _ in range(N)]
queue = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            ans[i][j] += 1
        if not arr[i][j]:
            count = 1
            walls = []
            queue = [[i, j]]
            while queue:
                x0, y0 = queue.pop()
                arr[x0][y0] = -1
                for d in range(4):
                    x1 = x0+dx[d]
                    y1 = y0+dy[d]
                    if 0 <= x1 < N and 0 <= y1 < M:
                        if arr[x1][y1] > 0 and not wall_visited[x1][y1]:
                            wall_visited[x1][y1] = 1
                            walls.append([x1, y1])
                        elif not arr[x1][y1] and not visited[x1][y1]:
                            arr[x1][y1] = -1
                            visited[x1][y1] = 1
                            queue.append([x1, y1])
                            count += 1
            for wall in walls:
                x, y = wall
                ans[x][y] += count
                wall_visited[x][y] = 0
                ans[x][y] %= 10
for i in range(N):
    res = ''
    for j in range(M):
        res += str(ans[i][j] % 10)
    print(res)
