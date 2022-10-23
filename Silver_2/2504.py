S = list(input())
stack = []
answer = 0
temp = 1
for i in range(len(S)):
    if S[i] == '(':
        stack.append('(')
        temp *= 2
    elif S[i] == '[':
        stack.append('[')
        temp *= 3
    elif S[i] == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break
        if S[i-1] == '(':
            answer += temp
        stack.pop()
        temp //= 2
    else:
        if not stack or stack[-1] == '(':
            answer = 0
            break
        if S[i-1] == '[':
            answer += temp
        stack.pop()
        temp //= 3
if stack:
    print(0)
else:
    print(answer)
