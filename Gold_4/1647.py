import sys
import heapq


def Prim():
    visited = [0]*(N+1)
    result = []
    queue = []
    heapq.heappush(queue, (0, 1))
    while queue:
        cost, current = heapq.heappop(queue)
        if len(result) == N:
            break
        if not visited[current]:
            visited[current] = 1
            result.append(cost)
            for next, acc in route[current]:
                heapq.heappush(queue, (acc, next))
    return sum(result)-max(result)


input = sys.stdin.readline
N, M = map(int, input().split())
route = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    route[A].append([B, C])
    route[B].append([A, C])
print(Prim())