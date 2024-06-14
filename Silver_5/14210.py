keyboard = ["***ABCDE", "FGHIJKLM", "NOPQRSTU", "VWXYZ***"]
N = int(input())
words = [input() for _ in range(N)]
first = input()
ans = []
for word in words:
    if word.startswith(first):
        ans.append(word[len(first)])
for i in keyboard:
    for j in i:
        if j in ans:
            print(j, end='')
        else:
            print('*', end='')
    print()
