n, k = map(int, input().split())
coin = [int(input()) for i in range(n)]
coin.sort()
dp = [0]+[100000]*k
for i in coin:
    for j in range(i, k+1):
        dp[j] = min(dp[j-i]+1, dp[j])
if dp[j] == 100000:
    print(-1)
else:
    print(dp[k])
