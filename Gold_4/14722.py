'''
정사각형
11부터 시작해서 nn까지 간다
딸기 초코 바나나 딸기 순서
마시거나 안마실수 있음
0은 딸기 1은 초코 2는 바나나
'''
N = int(input())
arr = [[0]*(N+1)]+[[0]+list(map(int, input().split())) for _ in range(N)]
dp = [[[0, 0, 0] for _ in range(N+1)] for _ in range(N+1)]
ans = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if arr[i][j] == 0:
            dp[i][j][0] = max(dp[i][j-1][2]+1, dp[i-1][j][2]+1)
        else:
            dp[i][j][0] = max(dp[i][j-1][0], dp[i-1][j][0])
        if arr[i][j] == 1 and dp[i][j][0] > dp[i][j][1]:
            dp[i][j][1] = max(dp[i][j-1][0]+1, dp[i-1][j][0]+1)
        else:
            dp[i][j][1] = max(dp[i][j-1][1], dp[i-1][j][1])
        if arr[i][j] == 2 and dp[i][j][1] > dp[i][j][2]:
            dp[i][j][2] = max(dp[i][j-1][1]+1, dp[i-1][j][1]+1)
        else:
            dp[i][j][2] = max(dp[i][j-1][2], dp[i-1][j][2])
# print(dp)
print(max(dp[N][N]))
