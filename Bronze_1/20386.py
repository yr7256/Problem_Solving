num = 1e9
while True:
    N = int(input())
    x0, y0, z0 = 0, 0, 0
    x1, y1, z1 = num, num, num
    if not N:
        break
    for _ in range(N):
        x, y, z, d = map(int, input().split())
        x0, y0, z0 = max(x, x0), max(y, y0), max(z, z0)
        x1, y1, z1 = min(x1, x+d), min(y1, y+d), min(z1, y+d)
    ans = (x1-x0)*(y1-y0)*(z1-z0)
    print(ans if ans > 0 else 0)
