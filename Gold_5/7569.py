# 3차원으로 bfs를 돌리자
import collections
import sys


def bfs():
    while queue:
        x0, y0, z0 = queue.popleft()
        for i in range(6):
            x1 = x0+dx[i]
            y1 = y0+dy[i]
            z1 = z0+dz[i]
            if 0 <= x1 < N and 0 <= y1 < M and 0 <= z1 < H and tomato[z1][x1][y1] == 0:
                tomato[z1][x1][y1] = tomato[z0][x0][y0]+1
                queue.append([x1, y1, z1])


input = sys.stdin.readline
M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(N)]
          for _ in range(H)]
count = 0
queue = collections.deque([])
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
# 좌표는 (x, y, z)가 편한데, 인덱스는 2차원일 때, [i][j]로 쓰는게 익숙해서 벌어진 일..
for i in range(N):
    for j in range(M):
        for k in range(H):
            if tomato[k][i][j] == 1:
                queue.append([i, j, k])
bfs()
for k in range(H):
    for i in range(N):
        for j in range(M):
            if tomato[k][i][j] == 0:
                print(-1)
                exit(0)
            count = max(count, tomato[k][i][j])
print(count-1)
