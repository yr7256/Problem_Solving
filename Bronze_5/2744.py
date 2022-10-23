s = input()
ans = ''
for i in s:
    if i.isupper():
        ans += i.lower()
    else:
        ans += i.upper()
print(ans)
