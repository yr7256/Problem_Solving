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


# '''
# \ : U->L, R->D, D->R, L->U
# / : U->R, R->U, D->L, L->D
# '''
# dir = ['U', 'R', 'D', 'L']
# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1]
# td, tr = [1, 0, 3, 2], [3, 2, 1, 0]


# def OOB(r, c):
#     global n, m
#     if r < 0 or r >= n or c < 0 or c >= m:
#         return True
#     return False


# n, m = map(int, input().split())
# space = [list(input().rstrip()) for _ in range(n)]
# pr, pc = map(int, input().split())
# pr -= 1
# pc -= 1

# ans_t, ans_d = 0, 0
# for d in range(4):
#     nr, nc, nd, c = pr, pc, d, 1
#     while True:
#         r1 = nr+dr[nd]
#         c1 = nc+dc[nd]
#         if r1 < 0 or r1 >= n or c1 < 0 or c1 >= m or space[r1][c1] == 'C':
#             break
#         nr += dr[nd]
#         nc += dc[nd]
#         if space[nr][nc] == '/':
#             nd = td[nd]
#         elif space[nr][nc] == '\\':
#             nd = tr[nd]
#         c += 1
#         if (nr, nc, nd) == (pr, pc, d):
#             print(dir[d])
#             print("Voyager")
#             exit(0)
#     if ans_t < c:
#         ans_t = c
#         ans_d = d
# print(dir[ans_d])
# print(ans_t)
