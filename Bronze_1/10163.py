arr = [[0]*1001 for _ in range(1001)]
N = int(input())
for i in range(N):
    x, y, w, h = map(int, input().split())
    for j in range(x, x+w):
        arr[j][y:y+h] = [i+1]*h
    arr[x][y] = i+1
ans = [0]*(N+1)
for i in range(1001):
    for j in range(1001):
        ans[arr[i][j]] += 1
for i in ans[1:]:
    print(i)
