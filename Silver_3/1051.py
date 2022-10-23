import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = []
result = 0
for _ in range(N):
    A.append(list(map(int, input().rstrip())))
for i in range(N):
    for j in range(M):
        for k in range(min(M, N)):
            if 0 <= i+k < N and 0 <= j+k < M:
                if A[i][j] == A[i][j+k] == A[i+k][j] == A[i+k][j+k]:
                    if result < k:
                        result = k
print((result+1)**2)
