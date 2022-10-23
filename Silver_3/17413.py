import sys
input = sys.stdin.readline
S = input().rstrip()
reverse = True
word = ''
answer = ''
for i in S:
    if reverse == True:
        if i == '<':
            reverse = False
            word += i
        elif i == ' ':
            word += i
            answer += word
            word = ''
        else:
            word = i+word
    else:
        word += i
        if i == '>':
            reverse = True
            answer += word
            word = ''
print(answer+word)
