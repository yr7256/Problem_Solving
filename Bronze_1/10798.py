board = [[0]*15 for i in range(5)]
for i in range(5):
    S = input()
    for j in range(len(S)):
        board[i][j] = S[j]
for i in range(15):
    for j in range(5):
        if board[j][i] == 0:
            continue
        else:
            print(board[j][i], end='')
