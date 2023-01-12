N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
r, c = 0, 0
for i in range(N):
    if 'X' not in arr[i]:
        r += 1
for j in range(M):
    if 'X' not in [arr[i][j] for i in range(N)]:
        c += 1
print(max(r, c))