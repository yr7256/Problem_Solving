import sys
input = sys.stdin.readline
N = int(input())
img = [list(map(int, input().split())) for _ in range(N)]
one = 0
zero = 0
m_one = 0


def P(x, y, n):
    global one, zero, m_one
    first = img[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if first != img[i][j]:
                n = n//3
                for k in range(3):
                    for l in range(3):
                        P(x+k*n, y+l*n, n)
                return
    if first == 1:
        one += 1
        return
    elif first == 0:
        zero += 1
        return
    else:
        m_one += 1
        return


P(0, 0, N)
print(m_one)
print(zero)
print(one)
