import sys
import heapq
input = sys.stdin.readline
N = int(input())
A = []
for _ in range(N):
    n = int(input())
    if n == 0:
        if A:
            print((heapq.heappop(A))*(-1))
        else:
            print(0)
    else:
        heapq.heappush(A, -n)
