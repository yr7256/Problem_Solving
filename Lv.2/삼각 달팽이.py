dx = [1, 0, -1]
dy = [0, 1, -1]


def solution(n):
    arr = [[0]*i for i in range(1, n+1)]
    x, y, d = -1, 0, 0
    count = 1
    check = 0
    switch = n
    while switch:
        x += dx[d]
        y += dy[d]
        arr[x][y] = count
        check += 1
        count += 1
        if check == switch:
            switch -= 1
            check = 0
            d = (d+1)%3
    return sum(arr, [])