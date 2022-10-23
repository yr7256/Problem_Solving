import sys
input = sys.stdin.readline
S = list(input().strip())
M = int(input())
s2 = []
for i in range(M):
    C = list(input().split())
    if C[0] == 'L' and len(S) != 0:
        s2.append(S.pop())
    elif C[0] == 'D' and len(s2) != 0:
        S.append(s2.pop())
    elif C[0] == 'B' and len(S) != 0:
        S.pop()
    elif C[0] == 'P':
        S.append(C[1])
print(''.join(S+list(reversed(s2))))
