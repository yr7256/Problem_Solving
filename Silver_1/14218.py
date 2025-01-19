# python3 6564ms pypy3 860ms
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())  # n:도시개수 m:도로개수
graph = [[0]*(n+1) for _ in range(n+1)]
distance = [-1]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())  # 도시
    graph[a][b] = 1
    graph[b][a] = 1
q = int(input())  # q:도로의 수
for _ in range(q):
    i, j = map(int, input().split())  # i-j 도로
    graph[i][j] = 1
    graph[j][i] = 1
    visited = [0]*(n+1)
    queue = deque([[1, 0]])
    while queue:
        curr, acc = queue.popleft()  # curr:현재도시 acc:방문횟수
        if distance[curr] < 0:
            distance[curr] = acc
        distance[curr] = min(distance[curr], acc)
        visited[curr] = 1  # 초기값 세팅
        for i in range(1, n+1):  # 도시 돌기, i : 목표 도시
            if graph[curr][i] == 1 and not visited[i]:
                queue.append([i, acc+1])
                visited[i] = 1
    print(*distance[1:])
