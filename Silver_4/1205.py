N, M, P = map(int, input().split())
if N == 0:
    print(1)
else:
    A = list(map(int, input().split()))
    if N == P and A[-1] >= M:
        print(-1)
    else:
        count = N+1
        for i in range(N):
            if A[i] <= M:
                count = i+1
                break
        print(count)
