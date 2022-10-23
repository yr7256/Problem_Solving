'''
프림과 다익스트라의 알고리즘이 비슷하기 때문에 프림을 사용
다만 다익스트라는 최단 거리를 나타내고, 프림은 최소 비용을 나타낸다
그렇기 때문에 결과값에 가장 짧은 경로 더해주기
'''
import heapq
import sys


def Prim():
    result = 0
    queue = []
    heapq.heappush(queue, (0, 1))
    while queue:
        cost, current = heapq.heappop(queue)
        if not visited[current]:
            visited[current] = 1
            result += cost
            for next, acc in route[current]:
                heapq.heappush(queue, (acc, next))
    return result


input = sys.stdin.readline
V, E = map(int, input().split())
route = [[] for _ in range(V+1)]
visited = [0]*(V+1)
for i in range(E):
    A, B, C = map(int, input().split())
    route[A].append([B, C])
    route[B].append([A, C])
print(Prim())
