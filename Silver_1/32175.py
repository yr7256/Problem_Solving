N, H = map(int, input().split())
arr = list(map(int, input().split()))
num = 1e9+7
dp = [0]*(H+1)
dp[0] = 1
for i in range(1, H+1):
    for cup in arr:
        if i >= cup:
            dp[i] += dp[i-cup]
    dp[i] %= num
print(int(dp[H]))
