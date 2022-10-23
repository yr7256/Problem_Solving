N, M = map(int, input().split())
image = [list(map(int, input())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = [[0, 0]]
image[0][0] = 1
while queue:
    x, y = queue.pop(0)
    for i in range(4):
        x1 = x+dx[i]
        y1 = y+dy[i]
        if 0 <= x1 < N and 0 <= y1 < M and image[x1][y1] == 1:
            image[x1][y1] = 0
            queue.append([x1, y1])
            image[x1][y1] = image[x][y]+1
print(image[N-1][M-1])
