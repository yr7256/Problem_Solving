import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
route = [[] for i in range(n+1)]
for i in range(n-1):
    a, b, c = map(int, input().split())
    route[a].append((b, c))
    route[b].append((a, c))


def dijkstra(start):
    queue = []
    distance = [INF]*(n+1)
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        cost, now = heapq.heappop(queue)
        if distance[now] < cost:
            continue
        for arr, dist in route[now]:
            if distance[arr] > cost+dist:
                distance[arr] = cost+dist
                heapq.heappush(queue, (cost+dist, arr))
    return distance


d = dijkstra(1)
node = d.index(max(d[1:]))
d1 = dijkstra(node)
answer = max(d1[1:])
print(answer)
