import sys


def dfs(start):
    visited[start] = 1
    dp[start][1] = 1
    for destination in route[start]:
        if not visited[destination]:  # 방문 안했으면
            dfs(destination)  # 또 들어감 (맨 밑에서부터 올라감)
            dp[start][0] += dp[destination][1]  # 얼x
            dp[start][1] += min(dp[destination][0], dp[destination][1])  # 얼


input = sys.stdin.readline
sys.setrecursionlimit(10**8)
N = int(input())
route = [[] for _ in range(N+1)]
for i in range(N-1):
    u, v = map(int, input().split())
    route[u].append(v)
    route[v].append(u)
dp = [[0, 0] for _ in range(N+1)]
visited = [0]*(N+1)
dfs(1)
print(min(dp[1][0], dp[1][1]))
'''
dfs(1)33
dfs(2)21        dfs(3)01 dfs(4)21
dfs(5)01 dfs(6)01        dfs(7)01 dfs(8)01
'''
