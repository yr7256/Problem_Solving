N = int(input())
S = input()
num = [int(input()) for _ in range(N)]
stack = []
for i in S:
    if i.isupper():
        stack.append(num[ord(i)-ord('A')])
    else:
        a = stack.pop()
        b = stack.pop()
        if i == '+':
            stack.append(b+a)
        elif i == '-':
            stack.append(b-a)
        elif i == '*':
            stack.append(b*a)
        elif i == '/':
            stack.append(b/a)
print('%.2f' % stack[0])
