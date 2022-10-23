import sys
import heapq
input = sys.stdin.readline
N = int(input())
M = int(input())
bus = [[] for i in range(N+1)]
city_cost = [sys.maxsize]*(N+1)
for i in range(M):
    A, B, C = map(int, input().split())
    bus[A].append((B, C))
start, end = map(int, input().split())


def bus_cost(start):
    queue = []
    heapq.heappush(queue, (0, start))
    city_cost[start] = 0
    while queue:
        past, now = heapq.heappop(queue)
        for arr, cost in bus[now]:
            if city_cost[arr] > past+cost:
                city_cost[arr] = past+cost
                heapq.heappush(queue, (past+cost, arr))


bus_cost(start)
print(city_cost[end])
