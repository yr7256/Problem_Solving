def dfs(x):
    global ans
    for x1 in (x-arr[x], x+arr[x]):
        if 0 < x1 <= n and not visited[x1]:
            ans += 1
            visited[x1] = 1
            dfs(x1)


n = int(input())
arr = [0]+list(map(int, input().split()))
s = int(input())
ans = 1
visited = [0]*(n+1)
dfs(s)
print(ans)
