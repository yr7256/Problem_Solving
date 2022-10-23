import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize
V, E = map(int, input().split())
K = int(input())
route = [[] for i in range(V+1)]
distance = [INF]*(V+1)
for i in range(E):
    u, v, w = map(int, input().split())
    route[u].append((v, w))


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
                heapq.heappush(queue, (cost+dist, arr))


dijkstra(K)
for i in range(1, V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
