def move(x, y):
    if x == 0:
        return 2
    elif abs(x-y) == 1 or abs(x-y) == 3:
        return 3
    elif abs(x-y) == 2:
        return 4
    else:
        return 1


MAX = 9876543210
command = list(map(int, input().split()))
dp = [[[MAX for _ in range(5)] for _ in range(5)] for _ in range(len(command))]
dp[0][0][0] = 0
# dp n번째 왼쪽 오른쪽
for k in range(len(command)-1):
    next = command[k]
    for i in range(5):
        for j in range(5):
            dp[k+1][next][j] = min(dp[k+1][next][j], dp[k][i][j]+move(i, next))
            dp[k+1][i][next] = min(dp[k+1][i][next], dp[k][i][j]+move(j, next))
ans = MAX
for i in dp[len(command)-1]:
    for j in i:
        ans = min(ans, j)
print(ans)
