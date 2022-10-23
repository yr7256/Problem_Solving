dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
N = int(input())
M = int(input())
arr = [[0]*N for _ in range(N)]
x, y = 0, 0
count = N*N
d = 0
x1, y1 = 0, 0
while count > 0:
    if 0 <= x < N and 0 <= y < N and not arr[x][y]:
        arr[x][y] = count
        count -= 1
    else:
        x -= dx[d]
        y -= dy[d]
        d = (d+1) % 4
    x += dx[d]
    y += dy[d]
    if count == M:
        x1, y1 = x, y
for i in arr:
    print(*i)
print(x1+1, y1+1)
