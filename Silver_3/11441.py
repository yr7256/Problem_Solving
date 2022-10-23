import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
dp = [A[0]]
for i in range(1, N):
    dp.append(dp[-1]+A[i])
dp.append(0)
M = int(input())
for _ in range(M):
    i, j = map(int, input().split())
    print(dp[j-1]-dp[i-2])
