import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    answer = 1
    queue = set([(x, y, board[x][y])])
    while queue:
        x0, y0, ans = queue.pop()
        answer = max(answer, len(ans))
        for i in range(4):
            x1 = x0+dx[i]
            y1 = y0+dy[i]
            if 0 <= x1 < R and 0 <= y1 < C and board[x1][y1] not in ans:
                queue.add((x1, y1, ans+board[x1][y1]))
    return answer


R, C = map(int, input().split())
board = [list(input().strip()) for i in range(R)]
print(bfs(0, 0))
