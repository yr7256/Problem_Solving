while True:
    N = int(input())
    if not N:
        break
    ans = 0
    for i in range(1, N+1):
        ans += (N-i+1)**2
    print(ans)