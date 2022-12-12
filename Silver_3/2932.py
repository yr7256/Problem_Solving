N, K = map(int, input().split())
for i in range(K):
    X, R, C = map(int, input().split())
    quotient = X // N
    remainder = X % N
    r = quotient - R
    c = remainder - C