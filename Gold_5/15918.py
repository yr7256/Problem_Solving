def dfs(x):
    global ans
    if x == 2*n+1:
        ans += 1
        print(arr)
        return
    if arr[x]:
        dfs(x+1)
    else:
        for i in range(n):
            if not visited[i+1] and x+i+2 < 2*n+1 and not (arr[x] or arr[x+i+2]):
                visited[i+1] = 1
                arr[x] = i+1
                arr[x+i+2] = i+1
                dfs(x+1)
                visited[i+1] = 0
                arr[x] = 0
                arr[x+i+2] = i+1


n, x, y = map(int, input().split())
arr = [0]*(2*n+1)
visited = [0]*(n+1)
arr[x] = arr[y] = y-x-1
visited[y-x-1] = 1
ans = 0
dfs(1)
print(ans)
