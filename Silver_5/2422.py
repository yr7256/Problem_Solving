from itertools import combinations
N, M = map(int, input().split())
combi = list(combinations(range(1, N+1), 3))
dont = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    x, y = map(int, input().split())
    dont[x][y] = 1
    dont[y][x] = 1
answer = 0
for i in combi:
    if dont[i[0]][i[1]] or dont[i[0]][i[2]] or dont[i[1]][i[2]]:
        continue
    answer += 1
print(answer)
