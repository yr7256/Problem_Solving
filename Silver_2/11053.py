N = int(input())
A = list(map(int, input().split()))
dp = [1]*N
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j] and dp[i] < dp[j]+1:
            dp[i] = dp[j]+1
print(max(dp))
