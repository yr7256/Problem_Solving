from collections import deque
import sys
input = sys.stdin.readline
N, M, R = map(int, input().split())
arr = [[] for _ in range(N+1)]
visited = [0] * (N+1)
s = 1
for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)
queue = deque([R])
visited[R] = 1
while queue:
    curr = queue.popleft()
    arr[curr].sort(reverse=True)
    for dest in arr[curr]:
        if not visited[dest]:
            s += 1
            visited[dest] = s
            queue.append(dest)
for i in visited[1:]:
    print(i)
