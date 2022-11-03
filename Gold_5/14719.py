H, W = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0
for i in range(1, W-1):
    column = min(max(lst[:i]), max(lst[i+1:]))
    if column > lst[i]:
        ans += column - lst[i]
    # print(lst[:i], lst[i+1:])
    # print(column)
print(ans)
