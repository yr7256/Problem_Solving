import sys
import heapq


def dijkstra(start):
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
                heapq.heappush(queue, (distance[arr], arr))
    return distance


INF = sys.maxsize
N, M, K, X = map(int, input().split())
distance = [INF]*(N+1)
route = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    route[a].append((b, 1))
dijkstra(X)
# print(distance)
flag = True
for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        flag = False
if flag:
    print(-1)
