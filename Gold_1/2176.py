'''
일반적인 다익스트라 코드에 합리적인 경로 찾는 조건만 추가시켜줬다.
'''
import heapq
import sys


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    dist[start] = 0
    while queue:
        temp, current = heapq.heappop(queue)
        if dist[current] < temp:
            continue
        for target, length in route[current]:
            if dist[target] > temp+length:
                dist[target] = temp+length
                heapq.heappush(queue, (temp+length, target))
            if temp > dist[target]:
                dp[current] += dp[target]


input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
dist = [INF]*(N+1)
route = [[] for _ in range(N+1)]
dp = [0]*(N+1)
dp[2] = 1
for _ in range(M):
    A, B, C = map(int, input().split())
    route[A].append((B, C))
    route[B].append((A, C))
dijkstra(2)
# print(dist)
print(dp[1])
# print(route[1])