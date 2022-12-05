import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    numlst = [input().strip() for _ in range(n)]
    numlst.sort()
    flag = False
    for i in range(n-1):
        if numlst[i] in numlst[i+1][:len(numlst[i])]:
            flag = True
            break
    if flag:
        print('NO')
    else:
        print('YES')
    # print(numlst)