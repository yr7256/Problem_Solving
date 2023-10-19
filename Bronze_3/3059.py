alpha = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
T = int(input())
for _ in range(T):
    S = set(input())
    a = alpha-S
    ans = 0
    for i in a:
        ans += ord(i)
    print(ans)
