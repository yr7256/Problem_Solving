import sys
input = sys.stdin.readline
N = int(input())
user = set()
cnt = 0
for _ in range(N):
    word = input().strip()
    if word != 'ENTER':
        if word not in user:
            user.add(word)
            cnt += 1
    else:
        user.clear()
print(cnt)
