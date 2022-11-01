N = int(input())
dp = [[0]*N for _ in range(N)]
matrix = [list(map(int, input().split())) for _ in range(N)]
# 이 아이디어로 접근해보자. 늘어나게
for i in range(1, N):
    for start in range(N-i):
        end = start+i
        dp[start][end] = 2**32
        for mid in range(start, end):
            dp[start][end] = min(dp[start][end], dp[start][mid]+dp[mid+1]
                                 [end]+matrix[start][0]*matrix[mid][1]*matrix[end][1])

ans = 0
for i in dp:
    ans = max(ans, max(i))
print(ans)
