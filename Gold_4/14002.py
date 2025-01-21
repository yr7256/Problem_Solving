'''
boj 11053 가장 긴 증가하는 부분 수열
길이만 구하는 것 -> 가장 긴 증가하는 부분 수열 구하는 것
N = int(input())
A = list(map(int, input().split()))
dp = [1]*N
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j] and dp[i] < dp[j]+1:
            dp[i] = dp[j]+1
print(max(dp))
'''
N = int(input())
arr = list(map(int, input().split()))
dp = [[arr[i]] for i in range(N)]
for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j] and len(dp[i]) <= len(dp[j]):
            dp[i] = dp[j] + [arr[i]]
# ans = max(dp)
'''
반례
input
4
1 4 2 3
output
2
1 4
'''
ans = max(dp, key=len)
print(len(ans))
print(*ans)
