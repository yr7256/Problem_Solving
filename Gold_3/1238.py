import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize
N, M, X = map(int, input().split())
route = [[] for i in range(N+1)]
distance = [INF]*(N+1)
route2 = [[] for i in range(N+1)]
distance2 = [INF]*(N+1)
for i in range(M):
    a, b, c = map(int, input().split())
    route[a].append((b, c))
    route2[b].append((a, c))


def dijkstra(start, distance, route):
    queue = []
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


dijkstra(X, distance, route)
dijkstra(X, distance2, route2)
ans = 0
for i in range(1, N+1):
    ans = max(ans, distance[i]+distance2[i])
print(ans)
