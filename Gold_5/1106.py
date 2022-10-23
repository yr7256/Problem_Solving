C, N = map(int, input().split())
data = [[0, 0]]
for i in range(N):
    cost, client = map(int, input().split())
    data.append([cost, client])
data.sort()
dp = [[100000]*(C+1) for _ in range(N+1)]
for i in range(1, N+1):
    cost = data[i][0]
    client = data[i][1]
    for j in range(1, C+1):
        dp[i][j] = dp[i-1][j]
        k = 1
        while True:
            if j <= k*client:
                dp[i][j] = min(dp[i][j], k*cost)
                break
            else:
                dp[i][j] = min(dp[i][j], dp[i-1][j-k*client] + k*cost)
            k += 1
print(dp[N][-1])
print(dp)
