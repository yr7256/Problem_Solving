def tsp(start, current, acc, count):
    global ans
    if count == N:
        if arr[current][start]:  # 현재(마지막)에서 시작지점으로 갈 수 있다면
            ans = min(ans, acc+arr[current][start])  # 최소값 갱신 
        return
    if acc > ans:
        return
    for i in range(N):
        if arr[current][i] and not visited[i]:
            visited[i] = 1
            tsp(start, i, acc+arr[current][i], count+1)
            visited[i] = 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0]*N
ans = 10000000
for i in range(N):
    visited[i] = 1
    tsp(i, i, 0, 1)
    visited[i] = 0
print(ans)
