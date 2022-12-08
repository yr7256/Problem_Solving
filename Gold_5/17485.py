'''
밑으로만 간다
하지만 전에 움직인 방향으로는 못감
일단 arr 벽세우기
0으로는 안됨 101로 하자 (최대 원소의 값이 100이니까)
14722 우유배달처럼 dp안의 요소를 여러개 넣어보자
'''
import sys
input = sys.stdin.readline
MAX = sys.maxsize
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0, 0, 0] for _ in range(M+2)]] + [[[MAX, MAX, MAX]
                                         for _ in range(M+2)] for _ in range(N)]
for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j][0] = min(dp[i-1][j+1][1], dp[i-1][j+1][2]) + arr[i-1][j-1]
        dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + arr[i-1][j-1]
        dp[i][j][2] = min(dp[i-1][j-1][0], dp[i-1][j-1][1]) + arr[i-1][j-1]
ans = MAX
for fuels in dp[N]:
    for fuel in fuels:
        ans = min(ans, fuel)
print(ans)
