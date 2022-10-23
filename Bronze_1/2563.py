n = int(input())
square = [[0]*100 for i in range(100)]
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            square[i][j] = 1
answer = 0
for i in range(100):
    for j in range(100):
        if square[i][j]:
            answer += 1
print(answer)
