from itertools import permutations
N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
result = permutations(A, M)
for i in result:
    print(*i)
