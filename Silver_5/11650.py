import sys
N = int(sys.stdin.readline())
A = []
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))
A.sort(key=lambda x: (x[0], x[1]))
for i in A:
    print(i[0], i[1])
