import sys
n = int(sys.stdin.readline())
stack = []
count = 1
ans = []
for _ in range(n):
    a = int(sys.stdin.readline())
    while count <= a:
        stack.append(count)
        count += 1
        ans.append('+')
    if stack[-1] == a:
        stack.pop()
        ans.append('-')
if len(stack) != 0:
    print('NO')
else:
    for i in ans:
        print(i)
