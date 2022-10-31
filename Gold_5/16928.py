N, M = map(int, input().split())
board = [i for i in range(101)]
visited = [0 for i in range(101)]
for _ in range(N):
    a, b = map(int, input().split())
    board[a] = b
for _ in range(M):
    a, b = map(int, input().split())
    board[a] = b


def bfs(v):
    queue = [v]
    visited[v] = 0
    while queue:
        v = queue.pop(0)
        for i in range(1, 7):
            n = v+i
            if n > 100:
                continue
            c = board[n]
            if visited[c] == 0:
                queue.append(c)
                visited[c] = visited[v]+1
                if c == 100:
                    return


bfs(1)
print(visited[100])
