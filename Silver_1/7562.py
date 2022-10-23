from collections import deque
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]
T = int(input())
for i in range(T):
    l = int(input())
    chess = [[0]*l for i in range(l)]
    x0, y0 = map(int, input().split())
    x, y = map(int, input().split())
    queue = deque()
    queue.append([x0, y0])
    while queue:
        x0, y0 = queue.popleft()
        if x0 == x and y0 == y:
            break
        for i in range(8):
            x1 = x0+dx[i]
            y1 = y0+dy[i]
            if 0 <= x1 < l and 0 <= y1 < l and chess[x1][y1] == 0:
                queue.append([x1, y1])
                chess[x1][y1] = chess[x0][y0]+1
    print(chess[x][y])
