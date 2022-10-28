import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
dp = [[0]*N for _ in range(N)]
for i in range(N):
    for start in range(N-i):
        end = start+i
        if start == end:
            dp[start][end] = 1
        elif lst[start] == lst[end]:
            if i == 1:
                dp[start][end] = 1
            elif dp[start+1][end-1] == 1:
                dp[start][end] = 1
M = int(input())
for i in range(M):
    S, E = map(int, input().split())
    print(dp[S-1][E-1])
