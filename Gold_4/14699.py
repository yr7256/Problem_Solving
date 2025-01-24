from collections import deque
N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
dp = [1]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    if arr[a] > arr[b]:
        graph[a].append(b)
    else:
        graph[b].append(a)
for i in range(1, N+1):
    queue = deque([[i, 1]])
    while queue:
        curr, acc = queue.popleft()
        for target in graph[curr]:
            if dp[target] < acc+1:
                queue.append((target, acc+1))
                dp[target] = acc+1
for i in range(1, N+1):
    print(dp[i])
