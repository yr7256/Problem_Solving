'''
아래 오른쪽위 오른쪽아래만 가능
'''
num = 1e9+7
N, M = map(int, input().split())
K = int(input())
dp = [[-1]*(M+1) for _ in range(N+2)]
for i in range(K):
    x0, y0 = map(int, input().split())
    dp[x0][y0] = 0
for i in range(N+1):
    dp[i][0] = 0
for j in range(M+1):
    dp[0][j] = 0
    dp[N+1][j] = 0
dp[1][1] = 1
for y in range(1, M+1):
    for x in range(1, N+1):
        if x == 1 and y == 1:
            continue
        if dp[x][y] == -1:
            if y % 2:
                dp[x][y] = int((dp[x-1][y]+dp[x][y-1]+dp[x-1][y-1]) % num)
            else:
                dp[x][y] = int((dp[x-1][y]+dp[x][y-1]+dp[x+1][y-1]) % num)
print(dp[3][4])
'''
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 0, 1], 
 [1, 1, 1, 1, 1], 
 [1, 1, 1, 1, 1]] 

[[0, 0, 0, 0, 0],
 [0, 1, 1, 1, 1], 
 [0, 1, 1, 0, 1], 
 [0, 1, 1, 1, 1], 
 [0, 0, 0, 0, 0]] 
'''
