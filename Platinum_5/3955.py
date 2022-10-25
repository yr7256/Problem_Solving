from math import gcd


def candy(x, y):
    x0, y0 = 1, 0
    x1, y1 = 0, 1
    while y != 0:
        Q = x//y
        x, y = y, x%y
        x0, y0, x1, y1 = x1, y1, x0-Q*x1, y0-Q*y1
    return y0 if y0>0 else y0+y1


t = int(input())
for _ in range(t):
    K, C = map(int, input().split())
    ans = 'IMPOSSIBLE'
    if gcd(K, C) == 1:
        if candy(K, C) <= 10**9:
            if C == 1:
                if K < 10**9:
                    ans = K+1
            else:
                ans = candy(K, C)
    print(ans)