N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s, e = 0, N-1
ans = 0
while s < e:
    if arr[s]+arr[e] >= M:
        ans += 1
        s += 1
        e -= 1
    else:
        s += 1
print(ans)
