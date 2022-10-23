from itertools import permutations
N = int(input())
A = permutations(range(1, N+1), N)
for i in A:
    print(*i)
