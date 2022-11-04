from collections import deque
N, K = map(int, input().split())
queue = deque([N])
visited = [0]*(100001)
while queue:
    a = queue.popleft()
    if a == K:
        break
    for i in (a-1, a+1, 2*a):
        if 0 <= i <= 100000 and not visited[i]:
            queue.append(i)
            visited[i] = visited[a]+1
print(visited[K])
