import sys
input = sys.stdin.readline


def dfs(x, y, z):
    if x < 0 or y < 0 or a[x][y]:
        return 0
    if dp[x][y][z]:
        return dp[x][y][z]
    if z == 0:
        dp[x][y][z] = dfs(x, y-1, 2)+dfs(x, y-1, 0)
    elif z == 1:
        dp[x][y][z] = dfs(x-1, y, 1)+dfs(x-1, y, 2)
    else:
        if 0 <= x-1 and 0 <= y-1 and a[x-1][y] == 0 and a[x][y-1] == 0:
            dp[x][y][z] = dfs(x-1, y-1, 0)+dfs(x-1, y-1, 1)+dfs(x-1, y-1, 2)
    return dp[x][y][z]


N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0 for _ in range(3)] for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1
dfs(N-1, N-1, 0), dfs(N-1, N-1, 1), dfs(N-1, N-1, 2)
print(sum(dp[N-1][N-1]))

# 시간초과
# def dfs(x, y, shape):
#     global answer
#     if x == N-1 and y == N-1:
#         answer += 1
#         return answer
#     if shape == 0 or shape == 2:
#         if y+1 < N:
#             if a[x][y+1] == 0:
#                 dfs(x, y+1, 0)
#     if shape == 1 or shape == 2:
#         if x+1 < N:
#             if a[x+1][y] == 0:
#                 dfs(x+1, y, 1)
#     if shape == 0 or shape == 1 or shape == 2:
#         if x+1 < N and y+1 < N:
#             if a[x+1][y] == 0 and a[x][y+1] == 0 and a[x+1][y+1] == 0:
#                 dfs(x+1, y+1, 2)


# N = int(input())
# a = [list(map(int, input().split())) for _ in range(N)]
# answer = 0
# dfs(0, 1, 0)
# print(answer)
