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
# print(arr)
