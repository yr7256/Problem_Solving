import sys
from heapq import heappop, heappush
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    num, s, e = map(int, input().split())
    arr.append([s, e])
arr.sort()
queue = []
for s, e in arr:
    if queue and queue[0] <= s:
        heappop(queue)
    heappush(queue, e)
print(len(queue))
