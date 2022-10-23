tri = [[1]*i for i in range(1, 31)]
for i in range(2, 30):
    for j in range(1, i):
        tri[i][j] = tri[i-1][j-1]+tri[i-1][j]
n, k = map(int, input().split())
print(tri[n-1][k-1])
