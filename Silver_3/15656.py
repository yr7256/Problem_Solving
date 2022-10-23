from itertools import product
N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
result = product(A, repeat=M)
for i in result:
    print(*i)
