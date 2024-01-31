A, B = map(int, input().split())
K, X = map(int, input().split())
ans = min(B, K+X) - max(A, K-X) + 1
if ans > 0:
    print(ans)
else:
    print('IMPOSSIBLE')
