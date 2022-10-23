'''
외장함수를 잘 활용하는 습관을 들이도록 합시다.
2차원 배열이라서 다익스트라 쓰는게 조금 어색했음.
dist도 2차원 배열로 만들고 델타탐색해서, 조건에 만족하는 값만 heapq에 넣어주기
'''
import heapq
import sys
from collections import deque


# def dijkstra():
#     queue = []
#     heapq.heappush(queue, (arr[0][0], 0, 0))
#     distance[0][0] = arr[0][0]
#     while queue:
#         cost, x, y = heapq.heappop(queue)
#         if distance[x][y] < cost:
#             continue
#         for i in range(4):
#             x1 = x+dx[i]
#             y1 = y+dy[i]
#             if 0 <= x1 < N and 0 <= y1 < N:
#                 if distance[x1][y1] > cost+arr[x1][y1]:
#                     distance[x1][y1] = cost+arr[x1][y1]
#                     heapq.heappush(queue, (cost+arr[x1][y1], x1, y1))

def dijkstra():
    distance[0][0] = arr[0][0]
    queue = deque([[0, 0]])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            x1 = x+dx[i]
            y1 = y+dy[i]
            if 0 <= x1 < N and 0 <= y1 < N:
                if distance[x1][y1] > distance[x][y]+arr[x1][y1]:
                    distance[x1][y1] = distance[x][y]+arr[x1][y1]
                    queue.append([x1, y1])


INF = sys.maxsize
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
tc = 0
while True:
    N = int(input())
    tc += 1
    arr = [list(map(int, input().split())) for _ in range(N)]
    distance = [[INF] * N for _ in range(N)]
    if N == 0:
        break
    dijkstra()
    print(f'Problem {tc}: {distance[N-1][N-1]}')
