T = int(input())
for i in range(T):
    N = int(input())
    nlist = set(map(int, input().split()))
    M = int(input())
    mlist = list(map(int, input().split()))
    for i in mlist:
        if i in nlist:
            print(1)
        else:
            print(0)
