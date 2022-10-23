N = int(input())
s = list(map(int, input().split()))
v = int(input())
ans = 0
for i in s:
    if i == v:
        ans += 1
print(ans)
