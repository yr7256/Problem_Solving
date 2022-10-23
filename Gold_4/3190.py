from collections import deque


N = int(input())
K = int(input())
field = [[0]*N for i in range(N)]
snake = deque([])
for i in range(K):
    r, c = map(int, input().split())
    field[r-1][c-1] = 1
L = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
time_lst = deque([])
for i in range(L):
    X, C = input().split()
    time_lst.append([int(X), C])


def turn(n):
    global d
    if n == 'D':
        d = (d+1) % 4
    else:
        d = (d-1) % 4


d = 0
count = 0
x, y = 0, 0
snake.append((x, y))
field[x][y] = 2
while True:
    count += 1
    x = x+dx[d]
    y = y+dy[d]
    if not 0 <= x < N or not 0 <= y < N:
        break
    if field[x][y] == 1:
        field[x][y] = 2
        snake.append((x, y))
    elif field[x][y] == 0:
        field[x][y] = 2
        snake.append((x, y))
        x_0, y_0 = snake.popleft()
        field[x_0][y_0] = 0
    elif field[x][y] == 2:
        break
    if len(time_lst) != 0 and time_lst[0][0] == count:
        ti, di = time_lst.popleft()
        turn(di)
print(count)
