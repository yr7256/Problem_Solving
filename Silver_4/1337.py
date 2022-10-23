import sys
input = sys.stdin.readline
N = int(input())
A = [int(input()) for _ in range(N)]
A = sorted(A)
count_list = []
for i in range(0, N):
    count = 0
    for j in range(A[i], A[i]+5):
        if not j in A:
            count += 1
    count_list.append(count)
print(min(count_list))
