'''
직접적으로 친구거나 한다리 건너서 친구인거 visited에 찍어주자.
그러고나서 한 행의 요소의 합은 그 사람의 2-친구의 수일 것이다.
k, i, j 위치에 신경쓰자.
'''
N = int(input())
arr = [input() for _ in range(N)]
ans = 0
visited = [[0]*N for _ in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if arr[i][j]=='Y' or (arr[i][k]=='Y' and arr[k][j]=='Y'):
                visited[i][j] = 1
for v in visited:
    ans = max(ans, sum(v))
print(ans)