'''
\ : U->L, R->D, D->R, L->U
/ : U->R, R->U, D->L, L->D
'''
dir = ['U', 'R', 'D', 'L']
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
p1, p2 = (3, 2, 1, 0), (1, 0, 3, 2)  # p1: \ , p2: /
N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
PR, PC = map(lambda x: x-1, map(int, input().split()))
ans_t, ans_d = 0, 0
for i in range(4):
    r, c, d, t = PR, PC, i, 1
    while True:
        r1, c1 = r+dx[d], c+dy[d]
        if (r1 >= N or r1 < 0) or (c1 >= M or c1 < 0) or arr[r1][c1] == 'C':
            break
        r += dx[d]
        c += dy[d]
        if arr[r][c] == '\\':
            d = p1[d]
        if arr[r][c] == '/':
            d = p2[d]
        t += 1
        if (r, c, d) == (PR, PC, i):
            print(dir[i])
            print('Voyager')
            exit()
    if ans_t < t:
        ans_d = i
        ans_t = t
print(dir[ans_d])
print(ans_t)
