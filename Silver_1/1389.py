import sys
input = sys.stdin.readline
N, M = map(int, input().split())
F = [[N]*N for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    F[x-1][y-1] = F[y-1][x-1] = 1
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                F[i][j] = 0
            else:
                F[i][j] = min(F[i][j], F[i][k]+F[k][j])
bacon = []
for i in F:
    bacon.append(sum(i))
print(bacon.index(min(bacon))+1)
