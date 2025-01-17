T = int(input())
for _ in range(T):
    K = int(input())
    nums = [0]+list(map(int, input().split()))
    dp = [[0]*(K+1) for _ in range(K+1)]
    prefix = [0] * (K+1)
    for i in range(1, K+1):
        prefix[i] = prefix[i-1]+nums[i]
    for k in range(1, K):
        for i in range(1, K-k+1):
            end = k+i
            temp = 1e9
            for j in range(i, end):
                temp = min(temp, dp[i][j] + dp[j+1][end])
            dp[i][j] = temp + prefix[end] - prefix[i]
    print(dp[1][K])