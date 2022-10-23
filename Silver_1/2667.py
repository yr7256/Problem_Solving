def bfs(x, y):
    queue = [[x, y]]
    image[x][y] = 0
    num_count = 1
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            x1 = x+dx[i]
            y1 = y+dy[i]
            if 0 <= x1 < N and 0 <= y1 < N and image[x1][y1] == 1:
                image[x1][y1] = 0
                queue.append([x1, y1])
                num_count += 1
    count.append(num_count)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N = int(input())
image = [list(map(int, input())) for _ in range(N)]
count = []
for i in range(N):
    for j in range(N):
        if image[i][j] == 1:
            bfs(i, j)
print(len(count))
for i in sorted(count):
    print(i)
