import heapq
import sys
from math import dist


def Prim():
    result = 0
    queue = []
    heapq.heappush(queue, (0, 1))
    while queue:
        cost, current = heapq.heappop(queue)
        if not visited[current]:
            visited[current] = 1
            result += cost
            for next, acc in route[current]:
                heapq.heappush(queue, (acc, next))
    return result


input = sys.stdin.readline
n = int(input())
route = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for i in range(n):
    A, B = map(float, input().split())
    route[i//n]+=[dist(A, B)]
    # route[(i+1)//n].append([i//n, dist(A, B)])
# print(Prim())
print(route)
