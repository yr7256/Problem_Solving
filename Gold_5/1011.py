T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    d = y-x
    n = 1
    while True:
        if d <= n*(n+1):
            break
        n += 1
    if d <= n**2:
        print(n*2-1)
    else:
        print(n*2)
