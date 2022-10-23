import sys
input = sys.stdin.readline
N, M = map(int, input().split())
image = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = 0
max_value = max(map(max, image))


def dfs(x, y, count, sum):
    global result
    if sum+max_value*(3-count) <= result:
        return
    if count == 3:
        result = max(result, sum)
        return
    else:
        for i in range(4):
            x1 = x+dx[i]
            y1 = y+dy[i]
            if 0 <= x1 < N and 0 <= y1 < M and visited[x1][y1] == 0:
                if count == 1:
                    visited[x1][y1] = 1
                    dfs(x, y, count + 1, sum + image[x1][y1])
                    visited[x1][y1] = 0
                visited[x1][y1] = 1
                dfs(x1, y1, count+1, sum+image[x1][y1])
                visited[x1][y1] = 0


for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 0, image[i][j])
        visited[i][j] = 0
print(result)
