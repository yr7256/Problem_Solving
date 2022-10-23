import sys
input = sys.stdin.readline
N = int(input())
img = [list(map(int, input().split())) for _ in range(N)]
w = 0
b = 0


def Quad(x, y, n):
    global w, b
    first = img[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if first != img[i][j]:
                n = n//2
                Quad(x, y, n)
                Quad(x, y+n, n)
                Quad(x+n, y, n)
                Quad(x+n, y+n, n)
                return
    if first == 1:
        b += 1
        return
    else:
        w += 1
        return


Quad(0, 0, N)
print(w)
print(b)
