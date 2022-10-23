'''
각 위치에서 다익스트라 사용 후, 그 이동경로가 m 보다 작으면 파밍하자.
temp 값 저장한 후에 ans랑 비교해서 갱신시켜주기.
'''
import heapq
import sys


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    dist[start] = 0
    while queue:
        acc, current = heapq.heappop(queue)
        if dist[current] < acc:
            continue
        for arr, cost in route[current]:
            if dist[arr] > acc+cost:
                dist[arr] = acc+cost
                heapq.heappush(queue, (acc+cost, arr))


input = sys.stdin.readline
INF = sys.maxsize
n, m, r = map(int, input().split())
items = [0]+list(map(int, input().split()))
route = [[] for i in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    route[a].append((b, l))
    route[b].append((a, l))
ans = 0
for i in range(1, n+1):
    dist = [INF]*(n+1)
    temp = 0
    dijkstra(i)
    for j in range(1, n+1):
        if dist[j] <= m:
            temp += items[j]
    ans = max(temp, ans)
print(ans)