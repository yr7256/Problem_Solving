def numcount(X, N):
    count = 0
    while X != 0:
        X = X//N
        count += X
    return count


n, m = map(int, input().split())
if m == 0:
    print(0)
else:
    print(min(numcount(n, 2)-numcount(m, 2)-numcount(n-m, 2),
              numcount(n, 5)-numcount(m, 5)-numcount(n-m, 5)))
