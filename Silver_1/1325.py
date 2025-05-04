import sys


def dfs(x):
    visited = [0]*(N+1)
    visited[x] = 1
    stack = [x]
    while stack:
        curr = stack.pop()
        for target in graph[curr]:
            if not visited[target]:
                visited[target] = 1
                stack.append(target)
    return sum(visited)


input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)
arr = [0] + [dfs(i) for i in range(1, N+1)]
max_val = max(arr)
for i in range(N+1):
    if arr[i] == max_val:
        print(i, end=' ')
