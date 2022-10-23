from itertools import combinations_with_replacement
N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
result = combinations_with_replacement(A, M)
B = []
for i in result:
    B.append(i)
B = sorted(set(B))
for i in B:
    print(*i)
