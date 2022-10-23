A, B = map(int, input().split())
S = [0]
for i in range(46):
    for j in range(i):
        S.append(i)
print(sum(S[A:B+1]))
