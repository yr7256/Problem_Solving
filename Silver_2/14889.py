from itertools import combinations
N = int(input())
S = [list(map(int, input().split())) for i in range(N)]
team = []
for i in list(combinations(range(N), N//2)):
    team.append(i)
gap = 1000
for a in team:
    stat_A = 0
    stat_B = 0
    for i in a:
        for j in a:
            stat_A += S[i][j]
    b = [i for i in range(N) if i not in a]
    for i in b:
        for j in b:
            stat_B += S[i][j]
    gap = min(gap, abs(stat_A-stat_B))
print(gap)
