import heapq
import sys


def dijkstra(start, end):
    dist = [INF]*(N+1)
    dist[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        temp, current = heapq.heappop(queue)
        if dist[current] < temp:
            continue
        for target, length in route[current]:
            if dist[target] > temp+length:
                dist[target] = temp+length
                heapq.heappush(queue, (dist[target], target))
    return dist[end]


INF = sys.maxsize
N, M = map(int, input().split())
route = [[] for _ in range(N+1)]
for _ in range(N-1):
    s, e, l = map(int, input().split())
    route[s].append([e, l])
    route[e].append([s, l])
for _ in range(M):
    s, e = map(int, input().split())
    print(dijkstra(s, e))
