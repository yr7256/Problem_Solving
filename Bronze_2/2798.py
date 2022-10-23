N, M = map(int, input().split())
A = list(map(int, input().split()))
B = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if A[i]+A[j]+A[k] > M:
                continue
            else:
                B = max(B, A[i]+A[j]+A[k])
print(B)
