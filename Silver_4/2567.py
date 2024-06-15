dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
N = int(input())
arr = [[0 for _ in range(101)] for _ in range(101)]
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1
cnt = 0
for i in range(101):
    for j in range(101):
        if arr[i][j]:
            for k in range(4):
                x1 = i+dx[k]
                y1 = j+dy[k]
                if not arr[x1][y1]:
                    cnt += 1
print(cnt)
