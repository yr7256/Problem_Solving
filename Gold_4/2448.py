N = int(input())
graph = [[' ']*(2*N-1) for i in range(N)]


def star(x, y, n):
    if n == 3:
        graph[x][y] = '*'
        graph[x+1][y-1] = '*'
        graph[x+1][y+1] = '*'
        for i in range(-2, 3):
            graph[x+2][y+i] = '*'
    else:
        half = n//2
        star(x, y, half)
        star(x+half, y-half, half)
        star(x+half, y+half, half)


star(0, N-1, N)
for i in graph:
    print(''.join(i))
