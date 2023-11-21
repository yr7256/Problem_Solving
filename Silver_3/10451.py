def dfs(x):
    visited[x] = 1
    dest = arr[x]
    if not visited[dest]:
        dfs(dest)
    return


T = int(input())
for _ in range(T):
    N = int(input())
    ans = 0
    arr = [0]+list(map(int, input().split()))
    visited = [0]*(N+1)
    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)
            ans += 1
    print(ans)
