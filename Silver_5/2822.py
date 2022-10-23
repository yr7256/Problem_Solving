S = []
for i in range(8):
    score = int(input())
    S.append((score, i+1))
S.sort(key=lambda x: (-x[0], x[1]))
num = 0
index = []
for i in range(5):
    num += S[i][0]
    index.append(S[i][1])
index.sort()
print(num)
print(*index)
