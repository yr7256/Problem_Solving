import sys
input = sys.stdin.readline
n = int(input())
# zero = 1
# one = 0
# temp = 0
# for _ in range(n):
#     temp = one
#     one = one+zero
#     zero = temp
# print((zero+one) % 10007)
dp = [0]*(n+1)
dp[0] = 1
for i in range(1, n+1):
    if i == 1:
        dp[i] = 1
    else:
        dp[i] = dp[i-1]+dp[i-2]
print(dp[n] % 10007)
