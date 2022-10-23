num = 1
while True:
    s = input()
    if '-' in s:
        break
    stack = []
    count = 0
    for i in s:
        if i == '{':
            stack.append('{')
        else:
            if stack:
                stack.pop()
            else:
                count += 1
                stack.append('-')
    count += len(stack)//2
    print('%d. %d' % (num, count))
    num += 1
