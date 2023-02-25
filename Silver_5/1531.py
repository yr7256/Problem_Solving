N, M = map(int, input().split())
pic = [[0]*100 for _ in range(100)]
for _ in range(N):
    x0, y0, x1, y1 = map(int, input().split())
    for i in range(x0-1, x1):
        for j in range(y0-1, y1):
            pic[i][j] += 1
ans = 0
for i in range(100):
    for j in range(100):
        if pic[i][j] > M:
            ans += 1
print(ans)
