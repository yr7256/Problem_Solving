N, M = map(int, input().split())
if N:
    books = list(map(int, input().split()))
    ans = 1
    acc = 0
    for i in range(N-1, -1, -1):
        acc += books[i]
        if acc > M:
            ans += 1
            acc = books[i]
    print(ans)
else:
    print(0)
