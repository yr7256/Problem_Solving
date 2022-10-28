import heapq
import sys
from math import dist


def Prim():
    result = 0
    queue = []
    heapq.heappush(queue, (0, 1))
    while queue:
        cost, current = heapq.heappop(queue)
        if current not in visited:
            visited.add(current)
            result += cost
            for next, acc in route[current]:
                heapq.heappush(queue, (acc, next))
    return result


input = sys.stdin.readline
n = int(input())
visited = set()
lst = []
route = [[] for _ in range(n+1)]
for i in range(n):
    x, y = map(float, input().split())
    lst.append([x, y])
for i in range(n):
    for j in range(i+1, n):
        route[i+1].append([j+1, dist(lst[i], lst[j])])
        route[j+1].append([i+1, dist(lst[i], lst[j])])
# print(route)
print(f'{Prim():.2f}')
