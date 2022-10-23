N = int(input())
count = 0
for i in range(N):
    S = input()
    stack = []
    for i in range(len(S)):
        if stack and S[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(S[i])
    if not stack:
        count += 1
print(count)
