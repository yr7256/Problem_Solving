import sys
K, N = map(int, sys.stdin.readline().split())
A = []
for _ in range(K):
    a = int(sys.stdin.readline())
    A.append(a)
L = 1
U = max(A)
while L <= U:
    M = (L+U)//2
    count = 0
    for i in A:
        count += i//M
    if count >= N:
        L = M+1
    else:
        U = M-1
print(U)
