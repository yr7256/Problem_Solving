from itertools import permutations
N = int(input())
A = list(map(int, input().split()))
lst = permutations(A)
answer = 0
for i in lst:
    s = 0
    for j in range(len(A)-1):
        s += abs(i[j]-i[j+1])
    answer = max(answer, s)
print(answer)
