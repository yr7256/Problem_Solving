dic = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)}
N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
status = [['S']*M for _ in range(N)]
ans = 0
for _ in range(R):
    X, Y, D = input().split()
    X, Y = int(X)-1, int(Y)-1
    x, y = map(int, input().split())
    x, y = x-1, y-1
    queue = [(X, Y)]
    status[X][Y] = 'F'
    ans += 1
    height = arr[X][Y]-1
    while True:
        X += dic[D][0]
        Y += dic[D][1]
        if 0 <= X < N and 0 <= Y < M and height > 0:
            if status[X][Y] == 'S':
                queue.append([X, Y])
                status[X][Y] = 'F'
                ans += 1
                height = max(height-1, arr[X][Y]-1)
            else:
                height -= 1
        else:
            break
    status[x][y] = 'S'
print(ans)
for i in status:
    print(*i)

