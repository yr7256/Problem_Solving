import sys
input = sys.stdin.readline
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
r1, c1, r2, c2 = map(int, input().split())
arr = [[0]*(c2-c1+1) for _ in range(r2-r1+1)]
x, y = 0, 0
d = 0
max_len = 0
len_count = 0
dcount = 1
num = 1
arr_count = (r2-r1+1)*(c2-c1+1)
while arr_count:
    if r1 <= x <= r2 and c1 <= y <= c2:
        arr[x-r1][y-c1] = num
        arr_count -= 1
        max_len = len(str(num))
    num += 1
    len_count += 1
    x += dx[d]
    y += dy[d]
    if dcount == len_count:
        len_count = 0
        d = (d+1) % 4
        if d == 0 or d == 2:
            dcount += 1
for i in arr:
    for j in i:
        print(str(j).rjust(max_len), end=' ')
    print()
    