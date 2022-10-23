D = [int(input()) for _ in range(9)]
S = sum(D)
for i in range(9):
    for j in range(i+1, 9):
        if 100 == S-(D[i]+D[j]):
            n, m = D[i], D[j]
D.remove(n)
D.remove(m)
D.sort()
for i in D:
    print(i)
