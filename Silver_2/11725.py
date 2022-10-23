import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
N = int(input())
tree = [[] for i in range(N+1)]
visited = [-1 for i in range(N+1)]
for i in range(N-1):
    A, B = map(int, input().split())
    tree[A].append(B)
    tree[B].append(A)


def dfs(X):
    for i in tree[X]:
        if visited[i] == -1:
            visited[i] = X
            dfs(i)


dfs(1)
for i in range(2, N+1):
    print(visited[i])
