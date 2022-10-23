from itertools import combinations_with_replacement
N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
result = combinations_with_replacement(A, M)
for i in result:
    print(*i)
