from heapq import heappush, heappop
import sys
input = sys.stdin.readline
N = int(input())
classes = [list(map(int, input().split())) for _ in range(N)]
classes.sort()
queue = [classes[0][1]]
for i in range(1, N):
    if classes[i][0] >= queue[0]:
        heappop(queue)
    heappush(queue, classes[i][1])
print(len(queue))
