import sys
input = sys.stdin.readline
N = int(input())
M = []
for _ in range(N):
    m = input().split()
    if m[0] == 'push':
        M.append(int(m[1]))
    elif m[0] == 'pop':
        if len(M) > 0:
            print(M.pop(0))
        else:
            print(-1)
    elif m[0] == 'size':
        print(len(M))
    elif m[0] == 'empty':
        if len(M) == 0:
            print(1)
        else:
            print(0)
    elif m[0] == 'front':
        if len(M) > 0:
            print(M[0])
        else:
            print(-1)
    elif m[0] == 'back':
        if len(M) > 0:
            print(M[-1])
        else:
            print(-1)
