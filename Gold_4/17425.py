import sys
input = sys.stdin.readline
dp = [0]*1000001
sum_dp = [0]*1000001
for i in range(1, 1000001):
    j = 1
    while i*j <= 1000000:
        dp[i*j] += i
        j += 1
for i in range(1, 1000001):
    sum_dp[i] = sum_dp[i-1]+dp[i]
T = int(input())
sum_lst = []
for i in range(T):
    N = int(input())
    sum_lst.append(sum_dp[N])
for i in sum_lst:
    print(i)


# import sys
# input = sys.stdin.readline
# dp = [0]*1000001
# sum_dp = [0]*1000001
# for i in range(1, 1000001):
#     for j in range(i, 1000001, i):
#         dp[j] += i
#     dp[i] += dp[i-1]
# T = int(input())
# for i in range(T):
#     N = int(input())
#     print(dp[N])
