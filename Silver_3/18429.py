from itertools import permutations, combinations
N, K = map(int, input().split())
A = list(map(int, input().split()))
count = 0
for tc in permutations(A, N):
    temp = 0
    for target in tc:
        temp += (target-K)
        if temp < 0:
            break
    else:
        count += 1
print(count)
