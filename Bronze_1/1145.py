s = list(map(int, input().split()))
s.sort()
ans = min(s)
while True:
    count = 0
    for i in range(len(s)):
        if ans % s[i] == 0:
            count += 1
    if count >= 3:
        print(ans)
        break
    ans += 1
