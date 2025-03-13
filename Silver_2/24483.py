import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(start, depth):
    global count, ans
    visited[start] = count*depth
    ans += visited[start]
    for destination in graph[start]:
        if visited[destination] == -1:
            count += 1
            dfs(destination, depth+1)


N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [-1]*(N+1)
count, ans = 1, 0
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(1, N+1):
    graph[i].sort()
dfs(R, 0)
print(ans)
