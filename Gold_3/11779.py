import sys
import heapq
import copy
input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
m = int(input())
bus = [[] for i in range(n+1)]
distance = [INF for i in range(n+1)]
path = [[] for i in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    bus[a].append((b, c))
start, end = map(int, input().split())
path[start].append(start)


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        cost, now = heapq.heappop(queue)
        if distance[now] < cost:
            continue
        for arr, dist in bus[now]:
            if distance[arr] > cost+dist:
                distance[arr] = cost+dist
                heapq.heappush(queue, (cost+dist, arr))
                path[arr] = []
                for i in path[now]:
                    path[arr].append(i)
                path[arr].append(arr)


dijkstra(start)
print(distance[end])
print(len(path[end]))
print(*path[end])
