def d(x, y, t):
    global M, m
    if x == N-1 and y == N-1:
        M = max(M, eval(t))
        m = min(m, eval(t))
        return
    if not (x+y) % 2:
        t = str(eval(t))
    if x < N-1:
        d(x+1, y, t+a[x+1][y])
    if y < N-1:
        d(x, y+1, t+a[x][y+1])


N = int(input())
a = [input().split() for _ in range(N)]
M = -5**5
m = 5**5
d(0, 0, a[0][0])
print(M, m)
