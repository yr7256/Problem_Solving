dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]
n = int(input())
check = [list(input()) for _ in range(n)]
curr = [list(input()) for _ in range(n)]
ans = [['.']*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if check[i][j] == '.' and curr[i][j] == 'x':
            cnt = 0
            for d in range(8):
                x1 = i+dx[d]
                y1 = j+dy[d]
                if 0 <= x1 < n and 0 <= y1 < n and check[x1][y1] == '*':
                    cnt += 1
            ans[i][j] = str(cnt)
        if check[i][j] == '*' and curr[i][j] == 'x':
            for k in range(n):
                for l in range(n):
                    if check[k][l] == '*':
                        ans[k][l] = '*'
for i in ans:
    print(''.join(i))
