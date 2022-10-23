n = int(input())
com = dict()
for i in range(n):
    p, l = map(str, input().split())
    if l == 'enter':
        com[p] = 1
    else:
        del com[p]
com = sorted(com.keys(), reverse=True)
for i in com:
    print(i)
