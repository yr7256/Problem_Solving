def stot(n):
    if n == S:
        return 1
    if len(n) < len(S):
        return 0
    ans = 0
    if n[-1] == 'A':
        ans = stot(n[:-1])
    if ans == 1:
        return 1
    if n[0] == 'B':
        s = n[::-1]
        ans = stot(s[:-1])
    return ans


S = input()
T = input()
ans = stot(T)
print(ans)
