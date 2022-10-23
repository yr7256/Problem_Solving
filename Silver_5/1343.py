S = input()
ans = ''
i = 0
while i < len(S):
    if S[i:i+4] == 'XXXX':
        ans += 'AAAA'
        i += 4
    elif S[i:i+2] == 'XX':
        ans += 'BB'
        i += 2
    elif S[i] == '.':
        ans += '.'
        i += 1
    else:
        break
if len(S) == len(ans):
    print(ans)
else:
    print(-1)
