import sys
input = sys.stdin.readline
# 되는 수 중에서 아무거나 넣고 다시 빼기 백트래킹
def sudoku(depth):
    if depth >= len(target):
        return False
    x0, y0 = target[depth][0], target[depth][1]
    candidate = possible_list(x0, y0)
    for c in candidate:
        arr[x0][y0] = c
        if not sudoku(depth+1):
            return False
        arr[x0][y0] = 0
    return True


# (x, y) 지점에서 되는 수만 집어 넣은 리스트 만들어보자
def possible_list(x, y):
    lst = []
    for i in range(1, 10):
        if is_possible(x, y, i):
            lst.append(i)
    return lst


# (x, y) 지점에서 num이 되냐 안되냐
def is_possible(x, y, num):
    for i in range(9):
        if arr[x][i] == num:
            return False
        if arr[i][y] == num:
            return False
    bx, by = x//3*3, y//3*3
    for i in range(bx, bx+3):
        for j in range(by, by+3):
            if arr[i][j] == num:
                return False
    return True


arr = []
target = []
for i in range(9):
    arr.append(list(map(int, input().split())))
    for j in range(9):
        if not arr[i][j]:
            target.append([i, j])
sudoku(0)
for i in arr:
    print(*i)