num = 1000000007
n = int(input())
dp = [1]*(n+1)
for i in range(2, n+1):
    dp[i] = (dp[i-2]+dp[i-1]+1) % num
print(dp[n])
