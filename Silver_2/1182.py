from itertools import combinations
N, S = map(int, input().split())
A = list(map(int, input().split()))
count = 0
for i in range(1, N+1):
    combi = combinations(A, i)
    for j in combi:
        if sum(j) == S:
            count += 1
print(count)
