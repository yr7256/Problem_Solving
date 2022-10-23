import sys
import collections
input = sys.stdin.readline
N, K = map(int, input().split())
queue = collections.deque([])
visited = [0]*(100001)
queue.append([N, 0])
while queue:
    a, b = queue[0][0], queue[0][1]
    if a == K:
        break
    queue.popleft()
    visited[a] = 1
    if 0 <= a-1 <= 100000 and visited[a-1] == 0:
        queue.append([a-1, b+1])
    if 0 <= a+1 <= 100000 and visited[a+1] == 0:
        queue.append([a+1, b+1])
    if 0 <= a*2 <= 100000 and visited[2*a] == 0:
        queue.append([2*a, b+1])
print(b)
