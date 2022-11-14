import sys
N = int(sys.stdin.readline())
A = []
for _ in range(N):
    a = list((map(int, sys.stdin.readline().split())))
    A.append(a)
A.sort(key=lambda x: (x[1], x[0]))
for i in A:
    print(i[0], i[1])
