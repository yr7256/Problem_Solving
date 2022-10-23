p = list(map(int, input()))
dp = [0 for i in range(len(p)+1)]
dp[0] = 1
dp[1] = 1
if p[0] == 0:
    print(0)
else:
    for i in range(2, len(p)+1):
        if p[i-1] > 0:
            dp[i] += dp[i-1]
        num = p[i-2]*10+p[i-1]
        if 10 <= num <= 26:
            dp[i] += dp[i-2]
    print(dp[len(p)] % 1000000)
