from itertools import combinations
N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
result = []
for i in list(combinations(A, M)):
    result.append(i)
result = sorted(list(set(result)))
for i in result:
    print(*i)
