'''
knuth optimization

DP[start][end] = min(DP[start][mid] + DP[mid+1][end]) + C[start][end] (start <= mid < end)
opt[i][j-1]<=opt[i][j]<=opt[i+1][j]

'''
# python3 시간초과 pypy3 1276ms
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    K = int(input())
    nums = [0]+list(map(int, input().split()))
    dp = [[0]*(K+1) for _ in range(K+1)]
    prefix = [0] * (K+1)
    for i in range(1, K+1):
        prefix[i] = prefix[i-1]+nums[i]
    for i in range(1, K):
        for start in range(1, K-i+1):
            end = start+i
            temp = 1e9
            for mid in range(start, end):
                temp = min(temp, dp[start][mid]+dp[mid+1][end])
            dp[start][end] = temp + prefix[end]-prefix[start-1]
    print(dp[1][K])
