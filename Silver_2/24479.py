import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(start):
    global count
    visited[start] = count
    for destination in graph[start]:
        if not visited[destination]:
            count += 1
            dfs(destination)


N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
count = 1
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(1, N+1):
    graph[i].sort()
dfs(R)
for i in range(1, N+1):
    print(visited[i])
