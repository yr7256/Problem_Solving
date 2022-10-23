import sys
input = sys.stdin.readline


def multi(N, X, Y):
    result = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += X[i][k]*Y[k][j]
            result[i][j] %= 1000
    return result


def devide(B, X):
    if B == 1:
        return X
    half = devide(B//2, X)
    if B % 2 == 0:
        return multi(N, half, half)
    else:
        return multi(N, multi(N, half, half), X)


N, B = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]
matrix = devide(B, A)
for row in matrix:
    for element in row:
        print(element % 1000, end=' ')
    print()
