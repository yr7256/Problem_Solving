import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize
N, E = map(int, input().split())
route = [[] for i in range(N+1)]
for i in range(E):
    a, b, c = map(int, input().split())
    route[a].append((b, c))
    route[b].append((a, c))
v1, v2 = map(int, input().split())


def dijkstra(start):
    queue = []
    distance = [INF]*(N+1)
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


d_1 = dijkstra(1)
d_v1 = dijkstra(v1)
d_v2 = dijkstra(v2)
result = min(d_1[v1]+d_v1[v2]+d_v2[N], d_1[v2]+d_v2[v1]+d_v1[N])
if result < INF:
    print(result)
else:
    print(-1)
