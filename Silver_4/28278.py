import sys
input = sys.stdin.readline
N = int(input())
stack = []
for _ in range(N):
    s = list(map(int, input().split()))
    if s[0] == 1:
        stack.append(s[1])
    if s[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    if s[0] == 3:
        print(len(stack))
    if s[0] == 4:
        print(0 if stack else 1)
    if s[0] == 5:
        print(stack[-1] if stack else -1)