import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))
queuestack = deque()
for i in range(N):
    if not A[i]:
        queuestack.appendleft(B[i])
for i in range(M):
    queuestack.append(C[i])
    print(queuestack.popleft(), end=' ')
