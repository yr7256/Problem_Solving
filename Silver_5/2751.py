import sys
N = int(sys.stdin.readline())
A = []
for _ in range(N):
    A.append(int(sys.stdin.readline()))
A = sorted(A)
for i in A:
    print(i)
