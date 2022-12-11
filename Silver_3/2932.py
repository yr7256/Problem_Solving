N, K = map(int, input().split())
for i in range(K):
    X, R, C = map(int, input().split())
    quotient = X // N
    remainder = X % N
    r = quotient - R
    c = remainder - C
    if r < 0:
        r += N
    if c < 0:
        c += N
    print(r,c)