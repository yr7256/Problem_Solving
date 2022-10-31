N = int(input())
dp = [[0]*N for _ in range(N)]
matrix = [list(map(int, input().split())) for _ in range(N)]
# 이 아이디어로 접근해보자.
for i in range(N):
    for start in range(N-i):
        end = start+i
        maxnum = 2**32
        for next in range(start, end):
            dp[start][end] = min(dp[start][end])


dp[start][0]*dp[next][1]*dp[end][1]
