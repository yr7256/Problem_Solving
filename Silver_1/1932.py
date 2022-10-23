import sys
input = sys.stdin.readline
n = int(input())
triangle = [list(map(int, input().split())) for i in range(n)]
k = 2
for i in range(1, n):
    for j in range(k):
        if j == 0:
            triangle[i][j] += triangle[i-1][j]
        elif j == i:
            triangle[i][j] += triangle[i-1][j-1]
        else:
            triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
    k += 1
print(max(triangle[n-1]))
