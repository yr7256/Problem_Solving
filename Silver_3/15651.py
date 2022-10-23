from itertools import product
N, M = map(int, input().split())
result = product(range(1, N+1), repeat=M)
for i in result:
    print(*i)
# for i in product(range(1, N+1), repeat=M):
#     print(' '.join(map(str, i)))
