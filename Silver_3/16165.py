N, M = map(int, input().split())
groups = {}
for i in range(N):
    group = input()
    num = int(input())
    groups[group] = []
    for i in range(num):
        mem = input()
        groups[group].append(mem)
for i in range(M):
    name = input()
    a = int(input())
    if a == 1:
        for g in groups:
            if name in groups[g]:
                print(g)
    else:
        for i in sorted(groups[name]):
            print(i)
