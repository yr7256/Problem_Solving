N, K = map(int, input().split())
if N < K*(K+1)//2:
    print(-1)
else:
    if (N-K*(K+1)//2) % K:
        print(K)
    else:
        print(K-1)
