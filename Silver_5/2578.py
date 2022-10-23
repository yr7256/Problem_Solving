def find(x):
    ans = 0
    for i in x:  # 가로줄
        if sum(i) == 0:
            ans += 1
    for i in range(5):  # 세로줄
        c = 0
        for j in range(5):
            if x[j][i] == 0:
                c += 1
        if c == 5:
            ans += 1
    d1 = 0
    for i in range(5):  # 우측 아래로 가는 대각선
        if x[i][i] == 0:
            d1 += 1
    if d1 == 5:
        ans += 1
    d2 = 0
    for i in range(5):  # 좌측 아래로 가는 대각선
        if x[i][4-i] == 0:
            d2 += 1
    if d2 == 5:
        ans += 1
    return ans


time = 0
bingo = [list(map(int, input().split())) for _ in range(5)]
ord = []  # 빙고는 알아보기 쉽게 5*5형태로, 불러주는건 쉽게 한줄로.
for i in range(5):
    ord += list(map(int, input().split()))
for s in range(25):
    for i in range(5):
        for j in range(5):
            if ord[s] == bingo[i][j]:
                bingo[i][j] = 0  # 사회자가 부른건 0으로.
                time += 1
                count = find(bingo)
                if count >= 3:
                    exit()
