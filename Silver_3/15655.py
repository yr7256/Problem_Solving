from itertools import combinations
N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
result = combinations(A, M)
for i in result:
    print(*i)
