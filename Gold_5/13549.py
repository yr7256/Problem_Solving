from collections import deque
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
queue = deque()
queue.append(N)
visited = [-1]*100001
visited[N] = 0
while queue:
    x = queue.popleft()
    if x == K:
        print(visited[x])
        break
    if 0 <= x-1 < 100001 and visited[x-1] == -1:
        visited[x-1] = visited[x]+1
        queue.append(x-1)
    if 0 <= x*2 < 100001 and visited[x*2] == -1:
        visited[x*2] = visited[x]
        queue.append(x*2)
    if 0 <= x+1 < 100001 and visited[x+1] == -1:
        visited[x+1] = visited[x]+1
        queue.append(x+1)
