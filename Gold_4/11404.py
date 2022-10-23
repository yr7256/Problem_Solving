import sys
input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
m = int(input())
bus = [[INF]*(n+1) for i in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    bus[a][b] = min(bus[a][b], c)
for k in range(1, n+1):
    bus[k][k] = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            bus[i][j] = min(bus[i][j], bus[i][k]+bus[k][j])
for i in range(1, n+1):
    for j in range(1, n+1):
        if bus[i][j] == INF:
            print(0, end=' ')
        else:
            print(bus[i][j], end=' ')
    print()
