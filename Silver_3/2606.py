N = int(input())
M = int(input())
route = [[0]*(N+1) for i in range(N+1)]
visited = [0]*(N+1)
A = []
for i in range(M):
    x, y = map(int, input().split())
    route[x][y] = route[y][x] = 1


def dfs(V):
    visited[V] = 1
    for i in range(1, N+1):
        if(visited[i] == 0 and route[V][i] == 1):
            A.append(i)
            dfs(i)
    return len(A)


print(dfs(1))
