from itertools import product
N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
result = []
for i in list(product(A, repeat=M)):
    result.append(i)
result = sorted(list(set(result)))
for i in result:
    print(*i)
