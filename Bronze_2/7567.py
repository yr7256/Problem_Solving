s = list(input())
ans = 0
for i in range(len(s)):
    if i == 0:
        ans += 10
    elif s[i] == s[i-1]:
        ans += 5
    else:
        ans += 10
print(ans)
