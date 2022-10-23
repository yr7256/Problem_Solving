def bfs(V):
    queue = [V]
    visited[V] = 0
    while queue:
        V = queue.pop(0)
        for i in range(1, n+1):
            if visited[i] == 0 and route[V][i] == 1:
                queue.append(i)
                visited[i] = visited[V] + 1


n = int(input())
m = int(input())
route = [[0]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)
for i in range(m):
    a, b = map(int, input().split())
    route[a][b] = 1
    route[b][a] = 1
bfs(1)
count = 0
for i in range(2, n+1):
    if 0 < visited[i] < 3:
        count += 1
print(count)
