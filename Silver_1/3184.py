from collections import deque


def bfs(x, y):
    queue = deque([[x, y]])
    o_cnt = 0
    v_cnt = 0
    while queue:
        x, y = queue.popleft()
        for i in range(5):
            x1 = x + dx[i]
            y1 = y + dy[i]
            if 0 <= x1 < R and 0 <= y1 < C and not visited[x1][y1]:
                if arr[x1][y1] == '#':
                    continue
                if arr[x1][y1] == 'v':
                    v_cnt += 1
                if arr[x1][y1] == 'o':
                    o_cnt += 1
                queue.append([x1, y1])
                visited[x1][y1] = 1
    return o_cnt, v_cnt


dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, 1, -1]
R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
s, w = 0, 0
for i in range(R):
    for j in range(C):
        if not visited[i][j] and arr[i][j] != '#':
            o_cnt, v_cnt = bfs(i, j)
            # print(o_cnt,v_cnt)
            if o_cnt > v_cnt:
                s += o_cnt
            else:
                w += v_cnt
print(s, w)
