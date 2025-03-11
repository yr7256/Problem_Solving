N = int(input())
arr = [list(input()) for _ in range(N)]
x, y = 0, 0
for i in range(N):
    cnt_x, cnt_y = 0, 0
    for j in range(N):
        if arr[i][j] == '.':
            cnt_x += 1
        else:
            cnt_x = 0
        if cnt_x == 2:
            x += 1
        if arr[j][i] == '.':
            cnt_y += 1
        else:
            cnt_y = 0
        if cnt_y == 2:
            y += 1
print(x, y)
