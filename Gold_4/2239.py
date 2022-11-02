# 되는 수 중에서 아무거나 넣고 다시 빼기 (빼는 근거 : 다음 수 들어갈 경우의 수 없을 때) 백트래킹
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
    arr.append(list(map(int, input())))
    for j in range(9):
        if not arr[i][j]:
            target.append([i, j])
sudoku(0)
for row in arr:
    print(''.join(map(str, row)))
# print(arr)


'''
가로 세로 상자 확인 (가로세로 확인은 쉽다)
상자 시작점은 x//3*3, y//3*3 - 함수 1

그리고 1~10까지 돌면서 그 지점에 되는 리스트 확인 - 함수 2

그 리스트로 스도쿠 돌아보자
어떻게? 일단 넣어보기
넣어보고 다음에 들어가는 요소가 0이 된다고 하면 다시 처음부터 돌아가자
아니라면 계속 진행하기 - 함수 3

다음에 들어가는 요소 확인해야 하니까 이중 for문으로 바로 확인하는 방법 어려움
그냥 스도쿠 돌릴 target list 하나 만들어서 depth 파서 들어가는 방법 사용하자
사전순 확인할 필요 x (숫자 넣을때 가로부터, 숫자도 오름차순으로 들어가기 때문이다)
str으로 받지말고 int로 받고 나중에 join할때 str으로 바꿔서 출력하기
'''
