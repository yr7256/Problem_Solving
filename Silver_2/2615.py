dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]
board = [list(map(int, input().split())) for _ in range(19)]
x0, y0 = 0, 0
ans = 0
for i in range(19):
    for j in range(19):
        if board[i][j]:
            point = board[i][j]
            for k in range(4):
                count = 1
                x1 = i + dx[k]
                y1 = j + dy[k]
                while 0 <= x1 < 19 and 0 <= y1 < 19 and board[x1][y1] == point:
                    count += 1
                    if count == 5:
                        if 0 <= x1+dx[k] < 19 and 0 <= y1+dy[k] < 19 and board[x1+dx[k]][y1+dy[k]] == point:
                            break
                        if 0 <= i-dx[k] < 19 and 0 <= j-dy[k] < 19 and board[i-dx[k]][j-dy[k]] == point:
                            break
                        print(point)
                        print(i+1, j+1)
                        exit()
                    x1 += dx[k]
                    y1 += dy[k]
print(0)


