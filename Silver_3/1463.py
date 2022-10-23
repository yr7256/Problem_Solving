import sys
input = sys.stdin.readline
X = int(input())
A = [0, 0, 1, 1]
for i in range(4, X+1):
    A.append(A[i-1]+1)
    if i % 2 == 0:
        A[i] = min(A[i//2]+1, A[i])
    if i % 3 == 0:
        A[i] = min(A[i//3]+1, A[i])
print(A[X])
