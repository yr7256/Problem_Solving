import sys
N, M = map(int, sys.stdin.readline().split())
A = []
P_A = []
for _ in range(N):
    a = sys.stdin.readline()
    A.append(a)
for i in range(N-7):
    for j in range(M-7):
        w = 0
        b = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if A[k][l] != 'W':
                        w += 1
                    else:
                        b += 1
                else:
                    if A[k][l] != 'B':
                        w += 1
                    else:
                        b += 1
        P_A.append(w)
        P_A.append(b)
print(min(P_A))
