P = int(input())
for _ in range(P):
    N, M = map(int, input().split())
    ans = 1
    l, r = 1, 1
    while True:
        if l == 0 and r == 1:
            break
        ans += 1
        l, r = r, (l+r) % M 
    print(N, ans)