import sys
input = sys.stdin.readline
keyboard = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"
while True:
    A = input().rstrip()
    result = ''
    if A == '':
        break
    for i in range(len(A)):
        if A[i] != ' ':
            result += keyboard[keyboard.index(A[i])-1]
        else:
            result += ' '
    print(result)
