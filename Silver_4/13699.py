n = int(input())
dp = [0]*36
dp[0], dp[1] = 1, 1
for i in range(2, n+1):
    if i % 2:
        for j in range(i//2):
            dp[i] += 2*dp[j]*dp[i-1-j]
        dp[i] += dp[i//2]**2
    else:
        for j in range(i//2):
            dp[i] += 2*dp[j]*dp[i-1-j]
print(dp[n])
