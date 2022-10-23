import sys
input = sys.stdin.readline
N = int(input())
board = [0] * N
count = 0


def check(X):
    for i in range(X):
        if board[X] == board[i] or abs(board[X]-board[i]) == abs(X-i):
            return False
    return True


def Queen(X):
    global count
    if X == N:
        count += 1
    else:
        for i in range(N):
            board[X] = i
            if check(X):
                Queen(X+1)


Queen(0)
print(count)
