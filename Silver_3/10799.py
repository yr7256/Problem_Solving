S = list(input())
stack = []
answer = 0
for i in range(len(S)):
    if S[i] == '(':
        stack.append('(')
    else:
        if S[i-1] == '(':
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer += 1
print(answer)
