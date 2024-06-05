import sys
input = sys.stdin.readline
N, K = map(int, input().split())
s = input().split()
temp = 0
for i in range(N):
    temp += len(s[i])

    if temp <= K:
        if i == 0:
            print(s[i], end='')
        else:
            print(' ' + s[i], end='')
    else:
        print()
        print(s[i], end='')
        temp = len(s[i])
print()
