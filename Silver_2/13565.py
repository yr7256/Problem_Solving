import sys
from collections import deque
input = sys.stdin.readline
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
M, N = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(M)]
for i in range(N):
    if not arr[0][i]:
        queue = deque([(0, i)])
        arr[0][i] = 2
        while queue:
            x, y = queue.popleft()
            for d in range(4):
                x1 = x+dx[d]
                y1 = y+dy[d]
                if 0 <= x1 < M and 0 <= y1 < N and not arr[x1][y1]:
                    queue.append((x1, y1))
                    arr[x1][y1] = 2
print("YES" if 2 in arr[-1] else "NO")
