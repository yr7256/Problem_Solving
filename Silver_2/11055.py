N = int(input())
A = list(map(int, input().split()))
dp = [i for i in A]
for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j]+A[i])
print(max(dp))
