import sys
input = sys.stdin.readline


def count(bomb):
    num = 0
    for i in range(N):
        count = 1
        for j in range(N-1):
            if bomb[i][j] == bomb[i][j+1]:
                count += 1
            else:
                count = 1
            num = max(num, count)
        count = 1
        for j in range(N-1):
            if bomb[j][i] == bomb[j+1][i]:
                count += 1
            else:
                count = 1
            num = max(num, count)
    return num


N = int(input())
bomb = [list(input()) for i in range(N)]
answer = 0
for i in range(N):
    for j in range(N):
        if j+1 < N:
            bomb[i][j], bomb[i][j+1] = bomb[i][j+1], bomb[i][j]
            num = count(bomb)
            answer = max(answer, num)
            bomb[i][j], bomb[i][j+1] = bomb[i][j+1], bomb[i][j]
        if i+1 < N:
            bomb[i][j], bomb[i+1][j] = bomb[i+1][j], bomb[i][j]
            num = count(bomb)
            answer = max(answer, num)
            bomb[i][j], bomb[i+1][j] = bomb[i+1][j], bomb[i][j]
print(answer)
