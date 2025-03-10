from itertools import combinations
from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
arr = [list(input()) for _ in range(5)]
ans = 0
for combi in combinations(range(25), 7):
    visited = [[0]*5 for _ in range(5)]
    x, y = combi[0] % 5, combi[0] // 5
    visited[x][y] = 1
    total, s = 0, 0
    queue = deque([[x, y]])
    while queue:
        x, y = queue.popleft()
        total += 1
        if arr[x][y] == 'S':
            s += 1
        for i in range(4):
            x1, y1 = x+dx[i], y+dy[i]
            if 0 <= x1 < 5 and 0 <= y1 < 5 and (x1+y1*5) in combi and not visited[x1][y1]:
                visited[x1][y1] = 1
                queue.append([x1, y1])
    if total == 7 and s >= 4:
        ans += 1
print(ans)
