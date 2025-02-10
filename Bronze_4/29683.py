n, a = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in arr:
    ans += i//a
print(ans)
